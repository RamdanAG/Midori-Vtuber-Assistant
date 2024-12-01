# modules/voicevox.py
# This module handles text-to-speech conversion using the Voicevox API.

import requests
from config import VOICEVOX_BASE_URL, DEFAULT_SPEAKER

def text_to_speech(text, speaker=DEFAULT_SPEAKER, output_path="outputs/output.wav"):
    """
    Uses Voicevox to generate audio from text.
    Args:
        text (str): The text to be converted into speech.
        speaker (int): The Voicevox speaker ID (default: DEFAULT_SPEAKER).
        output_path (str): The location to save the output audio file.
    """
    try:
        # Step 1: Create an audio query from the text
        params = {"text": text, "speaker": speaker}
        query_response = requests.post(f"{VOICEVOX_BASE_URL}/audio_query", params=params)
        query_response.raise_for_status()  # Check for errors from the API
        audio_query = query_response.json()

        # Step 2: Use the audio query to generate the audio file
        synthesis_response = requests.post(
            f"{VOICEVOX_BASE_URL}/synthesis",
            params={"speaker": speaker},
            json=audio_query,
        )
        synthesis_response.raise_for_status()  # Check for errors from the API

        # Step 3: Save the audio file to the output_path
        with open(output_path, "wb") as f:
            f.write(synthesis_response.content)
        print("Audio successfully created and saved at:", output_path)

    except requests.exceptions.RequestException as e:
        print(f"Error while using Voicevox API: {e}")
