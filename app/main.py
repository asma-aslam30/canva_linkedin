import os
import re
import urllib.parse
import requests
from pathlib import Path
from dotenv import load_dotenv

# ── NEW SDK ──────────────────────────────────────────────────────────────────
from google import genai
from google.genai import types

# ─────────────────────────────────────────────────────────────────────────────
SKILLS_DIR = Path(__file__).parent.parent / "skills"
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
def load_config():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌  GEMINI_API_KEY not found in .env – please add it.")
        return None
    return api_key


def read_skill(filename: str) -> str:
    path = SKILLS_DIR / filename
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# ─── STEP 1 : generate linkedin post + design spec ───────────────────────────
def generate_content(client, topic, audience, design_pref, brand_name, industry) -> str:
    linkedin_skill = read_skill("linkedin_post_skill.md")
    design_skill   = read_skill("design_optimization_skill.md")

    system_prompt = (
        "You are an expert content strategist and art director.\n"
        "Use the style and storytelling frameworks from the skill sets below, but OVERRIDE the templates.\n"
        "DO NOT provide options, recommendations, or rationales. Provide only the FINAL, polished, ready-to-post content.\n\n"
        f"--- LINKEDIN POST SKILL ---\n{linkedin_skill}\n\n"
        f"--- DESIGN OPTIMIZATION SKILL ---\n{design_skill}"
    )

    user_prompt = f"""
Generate the final, ready-to-post LinkedIn content and design specifications for:
- Topic:            {topic}
- Audience:         {audience}
- Design Preference:{design_pref}
- Brand Name:       {brand_name}
- Industry:         {industry}

Requirements:
1. Provide only ONE final version of the post.
2. No 'Option A/B/C', no 'Recommended Hook', no 'Rationale'.
3. The post must be ready to copy and paste directly.
4. Include final strategic hashtags.

At the end add a section called ## IMAGE GENERATION PROMPT
Write a single, self-contained image-generation prompt (max 120 words) that describes
a stunning LinkedIn graphic for this post. Include: canvas size 1080x1080,
dominant colour from the palette, hero headline text (≤8 words, in quotes),
visual style, and layout. No code – just the prompt text.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=system_prompt + "\n\n" + user_prompt,
    )
    return response.text


# ─── STEP 2 : extract the image prompt from the content ──────────────────────
def extract_image_prompt(content: str) -> str:
    match = re.search(
        r"##\s*IMAGE GENERATION PROMPT\s*\n+([\s\S]+?)(?:\n##|\Z)",
        content,
        re.IGNORECASE,
    )
    if match:
        return match.group(1).strip()
    # fallback – ask the model to build one from the full text
    return (
        "LinkedIn graphic, 1080x1080, dark navy background, bold white sans-serif "
        "headline 'AI Workflow Automated', electric-blue accent line, minimalist "
        "professional style, clean layout, subtle gradient."
    )


# ─── STEP 3 : generate the actual image ──────────────────────────────────────
def generate_image(image_prompt: str, brand_name: str) -> Path | None:
    print("\n🎨  Generating image using Open-Source Pollinations.ai …")
    print(f"   Prompt: {image_prompt[:100]}…")

    try:
        # Encode prompt for URL
        encoded_prompt = urllib.parse.quote(image_prompt)
        # Pollinations AI URL format: https://image.pollinations.ai/prompt/[prompt]?width=1080&height=1080&nologo=true
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1080&height=1080&nologo=true"
        
        response = requests.get(image_url, timeout=30)
        if response.status_code == 200:
            safe_brand = re.sub(r"[^a-z0-9_]", "_", brand_name.lower())
            out_path   = OUTPUT_DIR / f"linkedin_image_{safe_brand}.png"
            out_path.write_bytes(response.content)
            print(f"✅  Image saved → {out_path}")
            return out_path
        else:
            print(f"⚠️  Failed to fetch image. HTTP status: {response.status_code}")
            return None

    except Exception as exc:
        print(f"⚠️  Image generation failed: {exc}")
        print("   Falling back to Canva template URL …")
        return None


# ─── STEP 4 : canva deep-link (fallback / bonus) ─────────────────────────────
def canva_search_url(design_pref: str, topic: str) -> str:
    query = urllib.parse.quote(f"{design_pref} {topic} linkedin post template")
    return f"https://www.canva.com/templates?q={query}"


# ─────────────────────────────────────────────────────────────────────────────
def main():
    print("\n" + "=" * 55)
    print("🌟  CANVA × LINKEDIN AI CONTENT + IMAGE GENERATOR  🌟")
    print("=" * 55)

    api_key = load_config()
    if not api_key:
        return

    client = genai.Client(api_key=api_key)

    topic       = input("\n📝 Topic: ")
    audience    = input("👥 Target audience: ")
    design_pref = input("🎨 Design preference (e.g. Minimalist, Bold, Dark): ")
    brand_name  = input("🏢 Brand name: ")
    industry    = input("🏗️  Industry: ")

    # ── 1. Content + design spec ──────────────────────────────────────────────
    print("\n🚀 Running LinkedIn Post Skill + Design Optimization Skill …")
    content = generate_content(client, topic, audience, design_pref, brand_name, industry)

    print("\n" + "-" * 55)
    print("✅  GENERATED CONTENT")
    print("-" * 55)
    print(content)

    # Save as .txt file
    safe = re.sub(r"[^a-z0-9_]", "_", topic.lower())[:40]
    txt_path = OUTPUT_DIR / f"post_{safe}.txt"
    txt_path.write_text(content, encoding="utf-8")
    print(f"\n📄 Content saved → {txt_path}")
    
    # ── 2. Image generation ───────────────────────────────────────────────────
    image_prompt = extract_image_prompt(content)
    img_path     = generate_image(image_prompt, brand_name)

    # ── 3. Summary ────────────────────────────────────────────────────────────
    print("\n" + "=" * 55)
    print("🔗  RESULTS SUMMARY")
    print("=" * 55)
    print(f"📄 Content file   : {txt_path}")
    
    if img_path:
        print(f"🖼️  LinkedIn image  : {img_path}")
    else:
        url = canva_search_url(design_pref, topic)
        print(f"🔗 Canva templates : {url}")

    print("=" * 55)
    print("\n✨  Done!  Copy your post from the .txt file and attach the image on LinkedIn.")


if __name__ == "__main__":
    main()