#smarc #rnd 


# nepali tts

from transformers import VitsModel, AutoTokenizer
import torch
import scipy.io.wavfile
import numpy as np

# Load model and tokenizer
model = VitsModel.from_pretrained("procit001/nepali_male_v1")
tokenizer = AutoTokenizer.from_pretrained("procit001/nepali_male_v1")

# Input text
text = "म पनि जान्छु है त अहिले लाई"
inputs = tokenizer(text, return_tensors="pt")

# Generate waveform
with torch.no_grad():
    output = model(**inputs).waveform

# Convert waveform tensor to numpy and scale to int16 for WAV
waveform = output.squeeze().cpu().numpy()
waveform_int16 = np.int16(waveform / np.max(np.abs(waveform)) * 32767)

# Save as WAV file
scipy.io.wavfile.write("techno.wav", rate=model.config.sampling_rate, data=waveform_int16)

print("WAV file saved as 'techno.wav'")


this will work
if pos