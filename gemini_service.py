# gemini_service.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model (try different models if one doesn't work)
try:
    # Try newest model first
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception:
    try:
        # Fallback to older model
        model = genai.GenerativeModel('gemini-pro')
    except Exception:
        model = None

def get_gemini_response(prompt):
    """Get response from Gemini API"""
    if not model:
        return "Error: Gemini model not initialized. Please check your API key."
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        error_msg = str(e)
        if "API key" in error_msg:
            return "Error: Invalid or expired API key. Please check your Gemini API key."
        return f"Error: {error_msg}"

def get_astrology_reading(birth_details):
    """Generate astrology reading"""
    prompt = f"""You are a professional astrologer. Based on these birth details:
    
{birth_details}

Please provide a detailed astrology reading including:
1. Zodiac sign analysis
2. Planetary positions
3. Lucky numbers and colors
4. Career and relationship insights
5. General guidance for the upcoming period

Keep the response helpful, positive, and insightful."""
    
    return get_gemini_response(prompt)