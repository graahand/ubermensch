
# qwen-vl-2b extracted content

![[Pasted image 20251118004412.png]]
image_1


![[Pasted image 20251118005032.png]]
image_2: lfm2_vl_450m model extracted text

![[Pasted image 20251118010446.png]]
image_3:lfm2_vl_450m



## Progress Report Lead Data Entry OCR. 

### introduction to the project

The Lead Data Entry OCR project aims to develop a system that accurately extracts handwritten information from forms filled out by students. The information includes: name, class, faculty, phone number, guardian number, email, interested course, school name, who gave the seminar, rate us, and image_file_path.

### Objectives  

1. Correctly extract the information from the filled-out forms.
2. Generate a CSV file containing the extracted information from the filled-out forms.

---

### Tested OCR Tools and Models 

|                      |                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tool/Model Name      | Result/Verdict                                                                                                                                                                                                                                                                                                                                                                   |
| TrOCR                | This model was pre-trained on the IAM handwriting dataset. When tested with our samples, the results were unsatisfactory.                                                                                                                                                                                                                                                        |
| PaddleOCR            | This state-of-the-art OCR model, developed by PaddlePaddle, showed satisfactory results on our samples. It accurately detects form fields but struggles with recognizing handwritten characters—a limitation that could be improved by fine-tuning the text-recognition module with a larger, domain-specific dataset.                                                           |
| Mineru               | A PDF extraction tool that works well with digitally printed PDFs but performs poorly on image-based forms containing handwritten information like ours.                                                                                                                                                                                                                         |
| EasyOCR              | An open-source OCR model using CRAFT for detection and CRNN for recognition. It shows promising results on printed text but fails to reliably interpret handwritten content in our forms.                                                                                                                                                                                        |
| Qwen2-VL-2b          | A transformer-based vision-language model (VLM), distinct from traditional OCR systems. While not algorithmically designed for text extraction, it was trained on OCR and document parsing tasks. Early tests on a few handwritten samples showed promise, though it requires GPU resources and has slower processing times compared to dedicated OCR models. Tested via Ollama. |
| LFM2-VL-450M         | A smaller variant of LiquidAI’s vision-language model. Despite its size, initial tests on our sample forms yielded surprisingly promising results. The larger 3B-parameter version from LiquidAI could be evaluated and fine-tuned if needed for higher accuracy.                                                                                                                |
| Qwen3-VL-8B-Instruct | Tested on all 20 samples from the latest leads form format. Model size: 18 GB. Average processing time: 4.55 seconds per image. Delivers highly reliable extraction from handwritten forms.                                                                                                                                                                                      |
| Qwen3-VL-4B-Instruct | Tested on all 20 samples. Performance is on par with the 8B variant. Model size: 10 GB.                                                                                                                                                                                                                                                                                          |
| OlmOCR-7b            | Tested on a few sample images. Results were not sufficiently accurate or reliable for production use. Model size: 16 GB.                                                                                                                                                                                                                                                         |
| LFM2-VL-3B           | Evaluated on a small set of sample images. Results lacked the accuracy required for dependable data extraction.                                                                                                                                                                                                                                                                  |
| Deepseek-OCR         | Tested on a few images. The model is sensitive to prompt modifications—significant changes result in null outputs. With the default prompt, extraction accuracy was good but not perfect, falling slightly short of Qwen3-VL-8B-Instruct. Model size: 6 GB.                                                                                                                      |
### Dataset Collection and Annotation 

Dataset collection for this project was carried out in two phases.

In the first phase, we collected 30 form samples and created an annotated dataset containing approximately 280 lines of handwritten entries with corresponding annotations.

The second phase involved large-scale data collection. We gathered around 300 form samples and developed an annotated dataset comprising approximately 2,390 lines of sample images and their respective annotations.


### model finetuning and evaluation

The first-phase dataset (30 forms, ~280 annotated lines) was used to fine-tune the TrOCR model for 10 epochs. The results from the trained model were highly unsatisfactory. This may be due to either the limited size of the training data (only 280 samples) or the fact that TrOCR was pre-trained on scanned handwritten documents (like the IAM dataset), whereas our forms contain a mix of handwritten, digitally typed, and printed text (e.g., name, email, contact, course interest, school, faculty). 

In the next iteration, we fine-tuned PaddleOCR. Although this model was not originally pre-trained on handwritten data, we observed that it could accurately detect the location of text within the form—yet it struggled to correctly recognize the detected text, especially handwritten entries. To address this, we fine-tuned PaddleOCR using the IAM handwriting dataset for approximately 30 epochs. However, the results were underwhelming: the model failed to converge properly, and its performance degraded compared to the stock (pre-trained) version. 

In the latest iteration, we again fine-tuned PaddleOCR—but this time using only our in-house dataset. We collected and annotated 300 real student forms, which involved manually cropping each line from the form and transcribing its content. This yielded a dataset of approximately 2,400 annotated line images, which we used to train the text-recognition module of PaddleOCR v5 for 100 epochs.   

The model converged well, reaching a maximum character-level accuracy of 73%, with an aggregated loss of ~7.07 (CTC loss: 5.852, NRTR loss: 1.3118—lower is better). While we observed subtle improvements—such as better handling of handwriting variations among students—the overall performance was still worse than the stock model, making it unsuitable for reliable lead extraction in production. 

We then repeated the training using the larger 2,390-line dataset, this time applying four different image augmentation techniques (e.g., rotation, contrast adjustment, noise injection, elastic distortion) to diversify and expand the data. The model achieved a peak accuracy of 78%, with a slightly reduced total loss (5.108: CTC loss: 3.7913, NRTR loss: 1.3129). Despite the marginal numerical improvement, real-world performance on actual lead forms remained poor—significantly worse than the stock PaddleOCR model. Thus, augmentation did not yield the expected gains in this context. 

### Problem faced: 
1. **TrOCR limitations**: The model’s restricted context length (token limit), combined with its pre-training on pure handwriting datasets (e.g., IAM), proved unsuitable for our mixed-content forms—which include handwritten, typed, and printed text. This mismatch led to poor generalization and extraction failures.
    
2. **PaddleOCR dictionary conflict**: When fine-tuning PaddleOCR’s text recognition module with a custom dictionary (`dict.txt`) containing only the characters present in our dataset, we encountered severe internal layer conflicts—particularly in the CTC head. To resolve this, we reverted to training with the default dictionary, which includes a much broader set of characters, many of which do not appear in our data. This introduced unnecessary complexity: the model had to learn from a small set of ground-truth characters while being capable of predicting a far larger character set during training and inference, reducing efficiency and accuracy.
    
3. **Vision-Language Model (VLM) constraints**: While VLMs (e.g., Qwen-VL) can intelligently extract correct information from lead forms, they demand significant computational resources—**requiring GPU with sufficient VRAM** and cannot run on system RAM alone. Additionally, their decision-making is not transparent: we cannot easily interpret _why_ a specific value was extracted, making validation and error analysis difficult. Although these models could be fine-tuned on our dataset, **100% reliable extraction is not guaranteed** without extensive, rigorous training and testing—a barrier given current resource limitations.

### Purposed Solutions and Next Step 

Vision Language Models from Qwen are tested and found to be very accurate and reliable. Among them, **Qwen3-VL-4B-Instruct** offers the best trade-off between performance, model size (~10 GB), and extraction accuracy on handwritten lead forms—delivering results comparable to the larger 8B variant but with lower VRAM requirements.

Given these findings, our next step is to **integrate Qwen3-VL-4B-Instruct into a lightweight inference pipeline** that can process form images and output structured JSON responses containing all required fields (name, phone, course interest, etc.). We will wrap the model with a prompt-engineered template that explicitly asks for each field in a consistent format to improve output stability.

To address the **lack of interpretability**, we plan to log model inputs, prompts, and outputs alongside confidence indicators (e.g., repetition consistency) to enable basic validation. Additionally, we will explore **quantization** (e.g., GGUF or AWQ formats) to reduce memory footprint and enable potential deployment on mid-tier GPUS.


## alternative models vlms
1. internvl_3_5-8b (ocr score 840) [link to hf](https://huggingface.co/OpenGVLab/InternVL3_5-8B) [instruct model link](https://huggingface.co/OpenGVLab/InternVL3_5-8B-Instruct)
2. internvl3_9b (ocr score 877 )
3. qwen2_5-7b (ocr score 864)
4. internvl3_8b (ocr sscore 880)
5. glmvl3.5_9b (ocr score 823, docqa:80 ) [link](https://huggingface.co/zai-org/GLM-4.1V-9B-Thinking)
6. minicpm-v-4-4b (ocr score 862)
7. [openbmb/MiniCPM-V-4_5](https://huggingface.co/openbmb/MiniCPM-V-4_5)
8. [openbmb/MiniCPM-V-4](https://huggingface.co/openbmb/MiniCPM-V-4)
9. [RLAIF-V-12B](https://huggingface.co/openbmb/RLAIF-V-12B)
10. 
## qwen3-vl-instruct results

![/home/graahand/vlm-scratch/LeadsAutomation/input-dataset-final/WhatsApp Image 2025-11-19 at 3.03.30 PM.jpeg](file:///home/graahand/vlm-scratch/LeadsAutomation/input-dataset-final/WhatsApp%20Image%202025-11-19%20at%203.03.30%20PM.jpeg)
image_1
['{\n   
 "Name": "Biping Lai",\n    
 "class": "BSc",\n    
 "address": "taliipur dhapakhel",\n    
 "faculty": "computer security",\n    
 "phone number": "9108396857",\n    
 "guardian\'s number": "9815004202",\n    
 "email": "rdeony6@Gmail.com",\n    
 "interested course": "SEP",\n   
  "school name": "C EMS",\n    
  "who gave seminar": "lak",\n    
  "rate us": 5\n}']

![/home/graahand/vlm-scratch/LeadsAutomation/input-dataset-final/WhatsApp Image 2025-11-19 at 3.03.30 PM(1).jpeg](file:///home/graahand/vlm-scratch/LeadsAutomation/input-dataset-final/WhatsApp%20Image%202025-11-19%20at%203.03.30%20PM%281%29.jpeg)
image_2
['{\n    "Name": "Sanjeela Amatya",\n    
"class": "10",\n    
"address": "New Banesoor -31"
,\n    "faculty": "Management"
,\n    "phone number": "9877889922"
,\n    "guardian\'s number": "9822998277",
\n    "email": "sanjeelaamatya9880@gmail.com",
\n    "interested course": "GPPC",
\n    "school name": "Apex school",\
n    "who gave seminar": "Swapnil Sir",
\n    "rate us": 5\n}']
