import os
from pathlib import Path
from dotenv import load_dotenv

print("=" * 60)
print("API SETUP DEBUGGING")
print("=" * 60)

# Check current working directory
print(f"\n1. Current Working Directory: {os.getcwd()}")

# Check if .env file exists
env_path = Path.cwd() / ".env"
print(f"2. .env file exists: {env_path.exists()}")
if env_path.exists():
    print(f"   Path: {env_path}")
    with open(env_path, "r") as f:
        print(f"   Contents:\n{f.read()}")

# Load environment variables
print("\n3. Loading .env file...")
load_dotenv()

# Check if GEMINI_API_KEY is loaded
api_key = os.getenv("GEMINI_API_KEY", "")
print(f"4. GEMINI_API_KEY loaded: {bool(api_key)}")
if api_key:
    print(f"   Key (masked): {api_key[:10]}...{api_key[-10:]}")
    print(f"   Key length: {len(api_key)}")
else:
    print("   ERROR: No API key found!")

# Try to configure genai
print("\n5. Testing Google Generative AI configuration...")
try:
    import google.generativeai as genai
    
    if api_key:
        genai.configure(api_key=api_key)
        print("   ✓ genai.configure() successful")
        
        # Try to list available models
        print("\n6. Listing available models...")
        models = genai.list_models()
        model_count = 0
        for model in models:
            model_count += 1
            if model_count <= 5:
                print(f"   - {model.name}")
        print(f"   ... (total: {model_count} models)")
        
        print("\n✓ API KEY IS VALID AND WORKING!")
    else:
        print("   ERROR: No API key to configure")
        
except Exception as e:
    print(f"   ✗ Error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
