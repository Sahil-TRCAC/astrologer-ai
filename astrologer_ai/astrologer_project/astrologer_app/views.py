from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

GEMINI_API_KEY = "AIzaSyD1A3gosQ6Owzj3fSGGq7W8Z8Sc_09YQ84"

def home(request):
    return render(request, 'astrologer_app/home.html')

@csrf_exempt
def get_astrology_reading(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            system_prompt = data.get('system_prompt', '')
            user_question = data.get('user_question', '')
            
            prompt = f"""{system_prompt}

User Question: {user_question}

Respond as a professional astrologer:"""
            
            # Try different models in order
            models_to_try = [
                "gemini-2.5-flash",
                "gemini-2.0-flash", 
                "gemini-1.5-flash",
                "gemini-1.5-pro",
                "gemini-pro"
            ]
            
            answer = None
            used_model = None
            
            for model_name in models_to_try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={GEMINI_API_KEY}"
                
                payload = {
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }]
                }
                
                response = requests.post(url, json=payload)
                
                if response.status_code == 200:
                    result = response.json()
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    used_model = model_name
                    break
            
            if answer:
                return JsonResponse({
                    'success': True,
                    'answer': answer,
                    'model': used_model
                })
            else:
                return JsonResponse({
                    'success': False,
                    'error': 'No working model found'
                })
            
        except Exception as e:
            return JsonResponse({
                'success': False, 
                'error': str(e)
            })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)