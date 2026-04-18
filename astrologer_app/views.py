from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key (define it first!)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("API KEY loaded:", "Yes" if GEMINI_API_KEY else "No - Key missing!")

# Configure Gemini
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    # Use gemini-2.5-flash which worked in your test
    model = genai.GenerativeModel('gemini-2.5-flash')
    print("✅ Gemini model initialized with gemini-2.5-flash")
else:
    model = None
    print("❌ ERROR: GEMINI_API_KEY not found!")

def home(request):
    return render(request, 'astrologer_app/home.html')

@csrf_exempt
def get_astrology_reading(request):
    if request.method == 'POST':
        try:
            if model is None:
                return JsonResponse({
                    'success': False,
                    'error': 'API key not configured. Please check your .env file.'
                })
            
            data = json.loads(request.body)
            system_prompt = data.get('system_prompt', '')
            user_question = data.get('user_question', '')
            
            prompt = f"""{system_prompt}

User Question: {user_question}

Respond as a professional astrologer:"""
            
            # Generate response
            response = model.generate_content(prompt)
            
            return JsonResponse({
                'success': True,
                'answer': response.text
            })
                
        except Exception as e:
            print(f"Error in get_astrology_reading: {e}")
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)