# test_old_package.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(f"API Key exists: {bool(api_key)}")

if api_key:
    genai.configure(api_key=api_key)
    
    # Try with gemini-2.0-flash (available in your list)
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content("Say 'Hello World'")
        print(f"\n✅ Success with gemini-2.0-flash!")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"\n❌ Error with gemini-2.0-flash: {e}")
    
    # Try with gemini-2.5-flash as alternative
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content("Say 'Hello World'")
        print(f"\n✅ Success with gemini-2.5-flash!")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"\n❌ Error with gemini-2.5-flash: {e}")