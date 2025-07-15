# main.py
"""
Main controller script for the talkbot.
Integrates STT, TTS, LLM, personality, search, and memory to simulate conversation.
"""

import threading
from stt import STT
from tts import KokoroTTS
from llm import LLMPhi3Mini
from persona import Persona
from search_tool import SearchTool
from memory import Memory

def main():
    # Load components
    persona = Persona("jung_test.yaml")
    stt = STT()
    tts = KokoroTTS(
        model_path="kokoro-v1.0.int8.onnx",
        voice_path="voices-v1.0.bin",
        voice="af_heart", lang="en-us", speed=1.0
    )
    llm = LLMPhi3Mini(model_path="phi3-mini-q4_0.gguf")  # example model file
    search_tool = SearchTool()  # will use environment SERPAPI_KEY if set
    memory = Memory(max_buffer=4)
    
    def handle_speech(user_text: str):
        """
        Called whenever the STT module transcribes user speech.
        """
        print(f"User: {user_text}")
        # Check for tool-worthy queries
        query_lower = user_text.lower()
        if any(kw in query_lower for kw in ["who is", "what is", "where is", "how to", "nearby", "dental", "president"]):
            # Use search tool to get up-to-date info
            result = search_tool.search(user_text, num_results=2)
            reply = f"According to my search: {result}"
        else:
            # Construct prompt with persona and recent memory
            context = memory.get_buffer_text()
            persona_info = persona.summary()
            prompt = f"{persona_info}\n{context}\nUser: {user_text}\nBot:"
            # Generate response with LLM
            response = llm.generate(prompt, max_tokens=150, stop=["\n", "User:", "Bot:"], echo=False)
            reply = response.strip()
        # Add to memory and speak the reply
        memory.add(user_text, reply)
        print(f"Bot: {reply}")
        tts.speak(reply)
    
    # Start the speech recognition in the background
    print("Talkbot is listening... (say something)")
    stt.start_listening(handle_speech)
    
    # Keep the main thread alive
    try:
        while True:
            threading.Event().wait(1)
    except KeyboardInterrupt:
        print("Shutting down talkbot.")

if __name__ == "__main__":
    main()
