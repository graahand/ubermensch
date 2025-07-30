#rnd #echo

# robo 68

##  tts options
1. **kokoro tts**: 
	installation: 
		*pip   install -q kokoro>=0.9.2 soundfile
		apt-get --qq -y install espeak-ng > /dev/null 2>&1
	sample code:
	
		from kokoro import KPipeline
		from IPython.display import display, Audio
		import soundfile as sf
		import torch
		pipeline = KPipeline(lang_code='a')
		text = '''
		[Kokoro](/kˈOkəɹO/) is an open-weight TTS model with 82 million parameters. Despite its lightweight architecture, it delivers comparable quality to larger models while being significantly faster and more cost-efficient. With Apache-licensed weights, [Kokoro](/kˈOkəɹO/) can be deployed anywhere from production environments to personal projects.
		'''
		generator = pipeline(text, voice='af_heart')
		for i, (gs, ps, audio) in enumerate(generator):
		    print(i, gs, ps)
		    display(Audio(data=audio, rate=24000, autoplay=i==0))
		    sf.write(f'{i}.wav', audio, 24000)

	
2. **piper tts**(https://github.com/OHF-Voice/piper1-gpl): local neural tts. install it with `pip install piper-tts`.
	[check  out the voices samples here for english and nepali language](https://rhasspy.github.io/piper-samples/#en_US-ryan-high) 

* is it easy to integrate, implement?
	provides [c++](https://github.com/OHF-Voice/piper1-gpl/tree/main/libpiper) and [python api](https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/API_PYTHON.md) .

* resource usage? 
	uses medium resources(concrete details required...)
	
	installation: 
		pip install piper-tts
	sample code
		import wave
		`from piper import PiperVoice
		voice = PiperVoice.load("/path/to/en_US-lessac-medium.onnx")
		with wave.open("test.wav", "wb") as wav_file:
		voice.synthesize_wav("Welcome to the world of speech synthesis!", wav_file)
		
3. [orpheus-tts](https://www.google.com/search?q=orpheus+tts&ie=UTF-8): good natural sounding tts, provides finetuning options with excellent base model for testing and research purpose. 
* how hard to integrate?
	not much hard, a model needs to be loaded and accordingly the tts can be tweaked with provided parameters. 
* resource usage
	 need a thorough research
* installation:
	* git clone https://github.com/canopyai/Orpheus-TTS.git
	* cd Orpheus-TTS && pip install orpheus-speech # uses vllm under the hood 
	* pip install vllm==0.7.3
	* sample code:
		* from orpheus_tts import OrpheusModel
			import wave
			import time
			
			model = OrpheusModel(model_name ="canopylabs/orpheus-tts-0.1-finetune-prod", max_model_len=2048)
			prompt = '''Man, the way social media has, um, completely changed how we interact is just wild, right? Like, we're all connected 24/7 but somehow people feel more alone than ever. And don't even get me started on how it's messing with kids' self-esteem and mental health and whatnot.'''
			
			start_time = time.monotonic()
			syn_tokens = model.generate_speech(
			   prompt=prompt,
			   voice="tara",
			   )
			
			with wave.open("output.wav", "wb") as wf:
			   wf.setnchannels(1)
			   wf.setsampwidth(2)
			   wf.setframerate(24000)
			
			   total_frames = 0
			   chunk_counter = 0
			   for audio_chunk in syn_tokens: # output streaming
			      chunk_counter += 1
			      frame_count = len(audio_chunk) // (wf.getsampwidth() * wf.getnchannels())
			      total_frames += frame_count
			      wf.writeframes(audio_chunk)
			   duration = total_frames / wf.getframerate()
			
			   end_time = time.monotonic()
			   print(f"It took {end_time - start_time} seconds to generate {duration:.2f} seconds of audio")
### code tts_options


## stt options

1. [RealtimeSTT](https://github.com/KoljaB/RealtimeSTT): best tts based on whisper,best openly available stt that i have ever tested. resource hungry, PyTorch backend.
	`sudo apt-get update
	`sudo apt-get install python3-dev
	sudo apt-get install portaudio19-dev``
	pip install RealtimeSTT
	
2. [speechbrain](https://github.com/speechbrain/speechbrain) : another alternative for stt, easy to implement for inference with base pretrained models.`pip install speechbrain` 

## emotion detection options
1. [deepface](https://github.com/serengil/deepface) based on tensorflow, claimed to be lightweight

## wake word detection

1. RealtimeSTT provides porcupine based wake word detection.
to## llm options (backends and models)
### models
1. **qwen3-0.6b:** llama-server -hf unsloth/Qwen3-0.6B-GGUF:Q8_0o
2. **microsoft/Phi-3-mini-128k-instruct: llama-server -hf bartowski/Phi-3.1-mini-128k-instruct-GGUF:Q8_0
3. **Qwen/Qwen3-4B:**  llama-server -hf RefalMachine/RuadaptQwen3-4B-Instruct-GGUF:Q8_0
4. **Qwen/Qwen3-1.7B:** llama-server -hf unsloth/Qwen3-1.7B-GGUF:Q8_0
5. **dphn/Dolphin3.0-Llama3.2-3B:**  llama-server -hf mradermacher/Dolphin3.0-Llama3.2-3B-GGUF:Q8_0
6. **dphn/Dolphin3.0-Qwen2.5-0.5B: llama-server -hf mradermacher/Dolphin3.0-Qwen2.5-0.5B-GGUF:Q8_0


## challenges and consideration
1. how muchre

**procastination is vice to productivity but virtue to creativity**
generate more ideas as you can,that's the way to originals. 


 # robo68

phase 1: the robot at a core will be powered by a instruct ba
sed llm specifically finetuned for chatting and question answering, tuned/designed for engaging with the individual like chatgpt or siri. 

some of the models that can be used are: 

Note: the code should be functional containing only required functions (function for llm, function for tts, function for stt, function for timezone if required and if possible include function for search functionality to able to search real time information that the model can't provide). I don't want any docstring as well, only add the comments in the code where the code can be modified or replaced with any different value according to requirements. 


text-to-speech need to be implemented with the help of any open-source library (pyttsx3 at least) or any better and human sounding speech conversion. 

speech-to-text will be done using Realtimestt package openly available with github which can transcribe the human voice in real time.

flow: the large language model will be loaded using ollama (ollama run phi3:mini), realtimestt package will transcribe the speech from the user and text transcribed by this package will be passed to the llm as the input based on which the llm  will generate the output (conversation). then the text generated by the large language model will be converted into speech using the library mentioned above. the conversation will continue until and unless the user ask for ending it. 

i need to be able to provide the system prompt to the llm where i will specify its role as helpful robot which can provide answers to various questions along with providing the emotional supports to the users requiring conselling and information regarding the health. 

additionally use any python library to integrate the clock(time) for the robot. the timezone will be Nepal Standard Time (NST), which is UTC+5:45. based on time, the robot/llm should greet the user with good morning, good evening, good afternoon and so on. 


code snippet for realtimestt:
    pip install RealtimeSTT

    sudo apt-get update
    sudo apt-get install python3-dev
    sudo apt-get install portaudio19-dev

    from RealtimeSTT import AudioToTextRecorder
    import pyautogui

    def process_text(text):
        pyautogui.typewrite(text + " ")

    if __name__ == '__main__':
        print("Wait until it says 'speak now'")
        recorder = AudioToTextRecorder()

        while True:
            recorder.text(process_text)

    

use pttsx3 for text to speech which is faster.





discard speechbrain
system  prompt based on jung personality test 
realtimestt worked perfectly.  
ollama lib inference is best with 0.6b model. 

