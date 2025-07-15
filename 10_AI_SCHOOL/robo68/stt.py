# stt.py
"""
Real-time Speech-to-Text (STT) wrapper using RealtimeSTT.
This module listens to the microphone and transcribes speech into text in real time.
"""

from threading import Thread
from RealtimeSTT import AudioToTextRecorder

class STT:
    def __init__(self):
        """
        Initialize the STT recorder. Uses WebRTC and Silero VAD + Faster Whisper under the hood:contentReference[oaicite:17]{index=17}.
        """
        self.recorder = AudioToTextRecorder()  # low-latency transcription
        self.thread = None

    def _listen_loop(self, callback):
        """
        Internal loop: continuously record and transcribe speech, calling the callback with each transcription.
        """
        while True:
            # The recorder.text() method starts recording on voice activity and returns the text when done.
            text = self.recorder.text()  # blocks until phrase is detected
            if text:
                callback(text.strip())

    def start_listening(self, callback):
        """
        Start the background thread that listens to the microphone.
        The callback will be invoked with each transcribed text (string).
        """
        if self.thread is None:
            self.thread = Thread(target=self._listen_loop, args=(callback,), daemon=True)
            self.thread.start()
        else:
            print("STT listener is already running.")

# Example usage:
# def handle_text(text):
#     print("Heard:", text)
# stt = STT()
# stt.start_listening(handle_text)
