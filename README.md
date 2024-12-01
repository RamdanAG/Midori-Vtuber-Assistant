# Midori VTuber Assistant

Midori VTuber Assistant is a simple AI-powered assistant for VTubers. It integrates the **Google Gemini** API for generating AI responses and **Voicevox** for converting text to speech, allowing seamless interaction. This program supports text input from various sources like terminal windows, command prompts, or other interfaces. Future updates may include a more interactive UI for enhanced usability.

## Features
- **AI Response Generation**: Uses Google Gemini API to provide intelligent responses.
- **Text-to-Speech Conversion**: Converts text responses into natural-sounding audio using Voicevox.
- **Audio Playback**: Plays the generated audio directly.
- **Easy-to-Use**: Command-line interface for quick setup and usage.

## Installation

1. **Install Python**:
   Make sure Python (version 3.7 or higher) is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Set Up Voicevox**:
   - Install Voicevox software. You can download it from [Voicevox's official site](https://voicevox.hiroshiba.jp/).
   - Start the Voicevox engine locally or configure it with a server to enable API access.

3. **Install VTube Studio**:
   - Download and install VTube Studio from [VTube Studio's website](https://vtubestudio.com/).
   - Ensure your VTuber model is set up and ready for interaction.

4. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/midori-vtuber-assistant.git
   cd midori-vtuber-assistant
   ```

5. **Install Dependencies**:
   Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

6. **Configure API Endpoints**:
   - Open `config.py` and set the values for:
     - `VOICEVOX_BASE_URL`: The base URL of your Voicevox API.
     - `DEFAULT_SPEAKER`: The default speaker ID for Voicevox.
     - `GEMINI_API_KEY`: Your API key for Google Gemini (if applicable).

7. **Run the Program**:
   ```bash
   python main.py
   ```

## Usage

1. Start the program using the command above.
2. Enter your text input when prompted:
   - Example:
     ```
     You: Hello, Midori!
     AI: Hi there! How can I assist you today?
     ```
3. Listen to the generated audio response.
4. Type `exit` or `quit` to terminate the program.

## Future Enhancements
- **Interactive UI**: Develop a graphical user interface for easier interactions.
- **Multilingual Support**: Enable support for multiple languages.
- **Customization**: Add settings for voice pitch, speed, and other audio parameters.

## Contributing
Contributions are welcome! If you have ideas or improvements, feel free to fork the repository and submit a pull request.

## Acknowledgments
- **Google Gemini** for providing AI responses.
- **Voicevox** for the amazing text-to-speech API.
- **VTube Studio** for enabling seamless VTuber integration.
- The open-source community for inspiration and tools.

