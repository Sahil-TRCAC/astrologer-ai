from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import google.generativeai as genai


# Configure Gemini API using environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


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

            # Use stable model (don't guess multiple models)
            model = genai.GenerativeModel("gemini-1.5-flash")

            response = model.generate_content(prompt)

            return JsonResponse({
                'success': True,
                'answer': response.text
            })

        except Exception as e:
            print("Gemini ERROR:", e)

            return JsonResponse({
                'success': False,
                'error': str(e)
            })

    return JsonResponse({'error': 'Invalid request'}, status=400)