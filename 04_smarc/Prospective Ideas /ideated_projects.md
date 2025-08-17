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
11. 