# tts.py
"""
Kokoro Text-to-Speech (TTS) speaker.
Uses the Kokoro-onnx model to synthesize audio and plays it via speakers.
"""

import os
from kokoro_onnx import Kokoro
import sounddevice as sd

class KokoroTTS:
    def __init__(self, model_path="kokoro-v1.0.int8.onnx", voice_path="voices-v1.0.bin",
                 voice="af_heart", lang="en-us", speed=1.0):
        """
        Initialize the Kokoro TTS engine.
        :param model_path: path to the quantized Kokoro ONNX model (e.g., int8).
        :param voice_path: path to the voices .bin file.
        :param voice: voice preset name (e.g. 'af_heart' for English).
        :param lang: language code (e.g. 'en-us').
        :param speed: speaking speed (1.0 = normal).
        """
        # Load the Kokoro model
        self.kokoro = Kokoro(model_path, voice_path)
        self.voice = voice
        self.lang = lang
        self.speed = speed

    def speak(self, text: str):
        """
        Convert text to speech and play the audio via speakers (non-blocking).
        """
        # Generate audio samples and sample rate
        samples, sample_rate = self.kokoro.create(
            text, voice=self.voice, speed=self.speed, lang=self.lang
        )
        # Play the audio (this will block until playback is finished)
        sd.play(samples, sample_rate)
        sd.wait()

# Example usage:
# tts = KokoroTTS(model_path="kokoro-v1.0.int8.onnx", voice_path="voices-v1.0.bin")
# tts.speak("Hello, this is a test from Kokoro TTS.")
