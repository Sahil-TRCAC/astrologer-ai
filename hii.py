import requests

API_KEY = "AIzaSyD1A3gosQ6Owzj3fSGGq7W8Z8Sc_09YQ84"

# List all available models
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    models = response.json().get('models', [])
    print("Available Gemini Models:\n")
    for model in models:
        name = model.get('name', '').replace('models/', '')
        if 'gemini' in name.lower():
            print(f"✅ {name}")
            print(f"   Description: {model.get('description', 'N/A')[:80]}...")
            print(f"   Methods: {model.get('supported_generation_methods', [])}")
            print()
else:
    print(f"Error: {response.text}")