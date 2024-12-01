# main.py
# Main program to integrate Google Gemini and Voicevox.

from modules.gemini import get_response_gemini  # Gemini module for obtaining AI responses
from modules.voicevox import text_to_speech  # Voicevox module for TTS
from modules.audio import play_audio  # Module to play the resulting audio

def main():
    """
    Main program for the AI VTuber Assistant.
    Takes user input, generates a response using Gemini,
    and converts the response to speech using Voicevox.
    """
    print("AI VTuber Assistant is ready with Gemini. Type something to start...")

    while True:
        # Receive input from the user
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the program.")
            break

        # Send input to Gemini and get the response
        response = get_response_gemini(user_input)
        print(f"AI: {response}")

        # Convert the Gemini response to audio using Voicevox
        text_to_speech(response)

        # Play the audio through the device used by VTube Studio
        play_audio("outputs/output.wav")

if __name__ == "__main__":
    main()
