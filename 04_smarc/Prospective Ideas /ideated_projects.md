1. learnable machine (AI tool for education, teaching k-12 AI and computer science like code.org)


chatbot for bank's websites 


| siddhartha bank      | beesender | doesn't respond to message as well.                                                       |
| -------------------- | --------- | ----------------------------------------------------------------------------------------- |
| cgelectronics.com.np | palmmind  | works pretty well, list out the products as well, doesn't respond in nepali or romanized. |
| sanima bank          | palmmind  | respond to nepali or roman, answers queries correctly, speaks in english.                 |
| cimex nepal (byd)    |           | doesn't have any chatbot feature                                                          |
| hyundai              | palmmind  |                                                                                           |

perception-action agent
### tts

1. flow based generative models: think of flow models as pipes that can push water forward or backward- you can transform noise into voice and back gain smoothly (invertible)
2. codec-based networks: Codec models are like **neural MP3s** — they first shrink audio into a compact codebook, then treat speech as a sequence of “audio tokens” that can be modeled like words.
3. latent space means compressed representation of the data in lower dimensional form () where meaningful patterns are captured. Raw data like image of dimension 256 x 256 is of around  196,000 dimension, a 16 khz audio is equals to 16000 dimensions. Instead of thousands of pixel values, the latent vector might have just **128 or 512 numbers**. Each number captures some hidden attribute.
4. graphemes is the smallest written unit of language, like Word **“cat”** has graphemes **c**, **a**, **t**. graphemes deals with spelling not sound. 
5. phoneme is the smallest sound unit of language, how words are pronounced/spelled. Word **“cat”** has phonemes /k/, /æ/, /t/, phonemes is all about what you hear. 
6. prosody prediction required to make the tts less robotics by adding expression to the speech. for example: 
	 - Question: “You’re coming?” → rising pitch at the end.
    
	- Statement: “You’re coming.” → flat or falling pitch.
    
	- Same sentence, different prosody → different meaning/emotion.

7. timbre is that unique quality in the voice or sound of anything that can produce a sound, like piano and violin with exact same notes sounds different, two people speaking same words sounds different. timbre is what makes the voices unique. 
8. three main components of voice cloning: text-analysis(generated linguistic features from text), acoustic model (generates acoustic features[mel-spectrograms, pitch, duration, timbre info] from linguistic features[Word boundaries, stress, part-of-speech tags] or text/phonemes input, focusing on prosody and timbre) and vocoder which actually generates audio waveform using acoustic or linguistic features provided).
9. The **mel scale** is a frequency scale designed to match **human auditory perception**.The mel scale compresses high frequencies and spreads out low ones — more human-like.**mel-spectrogram** = a spectrogram where the frequency axis is warped into the **mel scale**.
10. Mel Frequency Cepstral Coefficients (MFCC)
11. Wavenet (chatgpt like model to generate raw audio waveforms sample by sample, uses **causal dilated convolutions** to capture long-range dependencies in audio.). later wavenet was repurposed from direct speech generator to vocoder (generating waveform audio from acoustic features(melspectrogram). produces speech that follows the given spectrogram.)
12. causal means (past and present not future). 
13. GAN-based vocoders like HiFi-GAN and MelGAN.
14. **HiFi-GAN and MelGAN** replaced WaveNet vocoder with GANs that generate waveforms in **parallel**: way faster, still natural-sounding.
15. TN-VQTTS, a novel TTS model that leverages timbre-normalized vector-quantized (TN-VQ) acoustic features for style-timbre disentanglement in speaker adaptation with limited data. This architecture consists of two main components: a txt2vec module that predicts TN-VQ features from input phonemes and a vec2wav module that uses those features, auxiliary prosodic features, and a speaker embedding from a conditioned speaker encoder to generate a speaker-specific waveform.
	1. *timbre-normalized means removing the speaker's unique voice quality and only extracting the main content, vector-quantized means compressing continuos features into finite set of discrete codes like a dictionary*
	2. *style-timbre disentanglement means seprating how someone speaks (emotional, fast/slow) and their unique voice quality, auxilary prosodic features means prosody means melody of speech, auxilary prosodic features means extra information like pitch, duration and energy that helps the model sound natural.*
	3. primary prosodic featueres are (pitch, duration and loudness)
		1. auxilary (supplemenatry) prosodic features 
			* formants, speaking rate, pause patterns, voice quality features (breathiness, creakiness and tension) and prosodic phrasing. 

	## speech fundamentals
	sound is just a air vibrating. ears catch those wiggles and brain says "oh that's a sound". frequency means how fast the air wiggles, where slow wiggles means deep sound (bass), fast wiggles means high sound (whistle, kid voice). when we talk out lungs push air and our vocal cords vibrate. based on those vibration our mouth, tongue, teeth and lips creates different sounds. this shaping of the vibration by (mttl) changes the spectrum of frequency. pitch means how high or low a voice sounds. loudness means how big or small vibrations (bigger vibration cause very loud shout). timbre is the unique particle that makes the sound unique from one another. prosody means expression while speaking (not being robotic). spetrogram means picture of how sound is being transmitted or spoken out. 

| auto-regressive tts models | non-autoregressive tts model            |
| -------------------------- | --------------------------------------- |
| tacotron (google)          | fastspeech and fastspeech 2 (microsoft) |
| tacotron 2 (google)        | flow-tts                                |
| deepvoice 2/3 (baidu)      | glow-tts                                |
| transformertts             | VITS                                    |
|                            | styletts and styletts2 (recent sota)    |


	