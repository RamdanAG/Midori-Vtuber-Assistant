# modules/audio.py
# This module handles audio playback using specific output devices (e.g., Virtual Audio Cable).

import pyaudio
import wave

def play_audio(file_path, output_device_name="CABLE Input (VB-Audio Virtual Cable)"):
    """
    Play a WAV audio file and direct the output to a specific audio device.
    Args:
        file_path (str): Path to the WAV audio file.
        output_device_name (str): Name of the audio device to be used for output.
    """
    try:
        # Open the audio file
        wf = wave.open(file_path, 'rb')
        audio = pyaudio.PyAudio()

        # Search for the output device by name
        output_device_index = None
        for i in range(audio.get_device_count()):
            device_info = audio.get_device_info_by_index(i)
            if output_device_name in device_info.get('name', ''):
                output_device_index = i
                break

        if output_device_index is None:
            raise ValueError(f"Audio device '{output_device_name}' not found.")

        # Open a stream for the appropriate device
        stream = audio.open(
            format=audio.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True,
            output_device_index=output_device_index
        )

        # Read and play audio data
        data = wf.readframes(1024)
        while data:
            stream.write(data)
            data = wf.readframes(1024)

        # Close the stream after completion
        stream.stop_stream()
        stream.close()
        audio.terminate()
        print("Audio playback completed.")
    except Exception as e:
        print(f"Error during audio playback: {e}")
