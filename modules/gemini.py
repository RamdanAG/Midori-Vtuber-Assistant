import requests
from config import GEMINI_API_KEY, GEMINI_API_URL

def get_response_gemini(prompt):
    """
    Sends a prompt to Google Gemini and retrieves a text response.
    Args:
        prompt (str): User's input text.
    Returns:
        str: Text response from Google Gemini.
    """
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "prompt": {
            "text": prompt
        },
        "temperature": 0.7,
        "candidateCount": 1
    }
    try:
        # Log the request for debugging
        print(f"Sending request to {GEMINI_API_URL} with payload: {payload}")

        # Send the request to the Gemini API
        response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error if the status is not 200

        # Parse the JSON response and return the output
        return response.json()["candidates"][0]["output"]
    except requests.exceptions.RequestException as e:
        # Log the error and API response for debugging
        print(f"An error occurred while accessing the Gemini API: {e}")
        if response is not None:
            print("API Response:", response.text)
        return "Sorry, an error occurred in the system."
