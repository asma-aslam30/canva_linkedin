import os
import google.generativeai as genai
from dotenv import load_dotenv
import urllib.parse

def load_config():
    """Loads configuration from .env file."""
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
    
    if not api_key:
        print("❌ Error: GEMINI_API_KEY not found in .env file. Please add it.")
        return None, None
    
    return api_key, model_name

def get_canva_search_url(query):
    """Generates a direct Canva search URL based on the design preferences."""
    encoded_query = urllib.parse.quote(query)
    return f"https://www.canva.com/templates?q={encoded_query}"

def generate_post_package(topic, audience, design_pref, brand_name, industry):
    """Calls the Gemini API to generate content and design specs using the provided skills."""
    api_key, model_name = load_config()
    if not api_key:
        return
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name)
    
    # We incorporate the content of our skill files as system instructions to the model
    # This ensures the model follows the rigid structural guidelines we defined earlier.
    with open("../skills/linkedin_post_skill.md", "r", encoding="utf-8") as f:
        linkedin_skill = f.read()
    with open("../skills/design_optimization_skill.md", "r", encoding="utf-8") as f:
        design_skill = f.read()
    
    system_prompt = f"""
    You are an expert content strategist and art director. 
    You must strictly follow the rules and output formats defined in these two skill sets:
    
    --- LINKEDIN POST SKILL ---
    {linkedin_skill}
    
    --- DESIGN OPTIMIZATION SKILL ---
    {design_skill}
    
    Your goal is to provide a complete package for the user.
    """
    
    user_prompt = f"""
    Please generate a complete LinkedIn post package and design guidelines based on the following:
    - Topic: {topic}
    - Audience: {audience}
    - Design Preference: {design_pref}
    - Brand Name: {brand_name}
    - Industry: {industry}
    
    In addition to the skill output, provide a 'Canva Template Search' section at the end 
    where you suggest 3 specific keywords to search for templates in Canva.
    """
    
    try:
        response = model.generate_content(system_prompt + "\n\n" + user_prompt)
        return response.text
    except Exception as e:
        return f"❌ API Error: {str(e)}"

def main():
    print("\n" + "="*50)
    print("🌟 CANVA-LINKEDIN CONTENT GENERATOR 🌟")
    print("="*50)

    # User Inputs
    topic = input("📝 Enter the main topic: ")
    audience = input("👥 Enter target audience: ")
    design_pref = input("🎨 Enter design preference (e.g., Minimalist, Bold): ")
    brand_name = input("🏢 Enter brand name: ")
    industry = input("🏗️ Enter industry: ")

    print("\n🚀 Generating your high-converting package... Please wait...")

    content = generate_post_package(topic, audience, design_pref, brand_name, industry)

    if content:
        print("\n" + "-"*50)
        print("✅ GENERATED CONTENT")
        print("-"*50)
        print(content)

        # Attempt to extract search terms and build a link
        # We use a simple heuristic: if the model suggests keywords, we'll build a link for the first one.
        # We build the Canva search URL based on the user's design preference and topic.
        canva_query = f"{design_pref} {topic} template"
        canva_link = get_canva_search_url(canva_query)

        print("\n" + "="*50)
        print("🔗 DIRECT CANVA ACCESS")
        print("="*50)
        print(f"Click here to find templates matching your style: {canva_link}")
        print("="*50)
    else:
        print("\n❌ Failed to generate content.")

if __name__ == "__main__":
    main()
