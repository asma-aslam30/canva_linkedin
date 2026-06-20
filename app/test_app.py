import os
from main import load_config, generate_content, extract_image_prompt, generate_image, OUTPUT_DIR
from google import genai
from pathlib import Path

def test_run():
    print("🧪 Starting Automation Test...")
    
    api_key = load_config()
    if not api_key:
        print("❌ API Key missing")
        return
    
    client = genai.Client(api_key=api_key)
    
    # Test Inputs
    test_data = {
        "topic": "AI in textiles and manufacturing",
        "audience": "Students",
        "design_pref": "Bold Navy Blue",
        "brand_name": "AI-Innovators",
        "industry": "Manufacturing"
    }
    
    print("🚀 Step 1: Generating Content...")
    content = generate_content(client, **test_data)
    print("✅ Content Generated.")
    
    print("🚀 Step 2: Saving to TXT...")
    safe = test_data["topic"].lower().replace(" ", "_")[:40]
    txt_path = OUTPUT_DIR / f"post_{safe}.txt"
    txt_path.write_text(content, encoding="utf-8")
    print(f"✅ Saved to {txt_path}")
    
    print("🚀 Step 3: Generating Image...")
    prompt = extract_image_prompt(content)
    img_path = generate_image(prompt, test_data["brand_name"])
    
    if img_path and img_path.exists():
        print(f"✅ Image Generated and Saved: {img_path}")
    else:
        print("❌ Image Generation Failed")

    print("\n🎉 Test Complete!")

if __name__ == "__main__":
    test_run()
