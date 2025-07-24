#llm #smarc #rnd
[[05_ai_maths]]
[[llms]]


# AI MATH EDUCTION

## requirements

1. individual model for each of the subject from nepali curriculum class 4 to class 12 {maths(questions and step by step solutions and conceptual understanding concepts,geometry and sets chapter is it feasible?, should include optional maths concepts and questions), nepali (question answer set and grammar rules with samples),english(questions answers and grammar rules, and english  writing samples), social (question answers samples from every chapter), science (question answers any science related concepts available within the weight of the base model.),}

2. training resources within PC resource plus google colab with compute resources (company won't be funding at all.)

3. framework PyTorch, HuggingfaceTransformer.

4. finetuning libraries (xtuner, unsloth, transformers)

5. inference backend (llama.cpp,vllm, triton server)

6. base models:  [GPT2-NEPALI](https://huggingface.co/Aananda-giri/GPT2-Nepali), [NepGPT2](https://huggingface.co/dinesh-bk/NepGPT2), [NepaliBERT](https://huggingface.co/Rajan/NepaliBERT), [and derivatives](https://huggingface.co/models?other=base_model:finetune:Rajan/NepaliBERT)

## Key considerations.

**garbage in garbage out**

dataset preparation should take maximum time but fixed and very actionable planing, one dataset, one model one evaluation at a time. we are starting with maths first from class 4 to class 10 first as the mathematics from class 11-12 is a bit more complex. 

base models should  be reasoning or not, i think reasoning is required but it also increases  the  resource requirement along the the throughput rate and latency. 

every subjects requires reasoning model.

**question answering is primary feature for this project but integration of pedagogy enhanced with AI is another feature. Such pedagogical philosophy for reflective and effective digital learning  is the main focus of mysecondteacher platform. This philosophy can be hugely impacted with the integration of efficient large language models along with AI assisted reflective and effective learning can be sun ma suganda.** 

**can we integrate the llms with the content of mysecondteacher videos lessons? students learns from video sessions and communicate with llms at the same time? this can be absolutely groundbreaking.** 

# dataset development

start with maths dataset, class four content, dataset development automated through a llm where a book is provided as a file performing Retrieval Augmented Generation for generating the questions-answer pairs along with important concepts and pedagogical and reflective learning emphasized. 

pdf reader package from python or any OCR technology for correct extraction of the text for vectorization and ......

key consideration: to preserve the way mathematics is expressed and solved unlike language subjects, we need to keep the symbols, flow, concepts intact for quality dataset

qwen2.5-math-7b-Instruct will be used for dataset generation or a large vision language model which can extract and generate efficently? i don't know whether the lvlm can work efficiently  in case? 
https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct



## prompts

write a python script that allow clipping the pdf file based on the page numbers, i mean to say i pass from what page to what page the pdf file's content is required, the script remove all other pages and only keep those pages that are mentioned or passed to the script. just a single function will be enough. 

Write a python script or multiple related scripts with their names that:
i. load a model using llama-cpp (llama-server -hf modelspace/modelname:q8_0)
ii. extract the text from the pdf file provided keeping the mathematical symbols and flow of solution intact.
	the  pdf file was a image-scanned pdf file which cannot be extracted with the pdf tools like pdfplumber of pypdf2 due to which use of OCR tool in extraction script is necessary. paddle OCR is one the best extraction package available for free. Let's use that  instead. 
	sample code for paddleOCR from original repository: 
	
	''' # Initialize PaddleOCR instance
	from paddleocr import PaddleOCR
	ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False)'''

# Run OCR inference on a sample image 
result = ocr.predict(
    input="https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_002.png")

# Visualize the results and save the JSON results
for res in result:
    res.print()
    res.save_to_img("output")
    res.save_to_json("output")


iii. based on the questions, question's solutions and concepts found in the pdf file, the task of the large language model is to create 10k maths question answer  pairs from that same pdf file provided to it. the pdf file provided to the model is a part of text book from Nepal's mathematics curriculum.
iv. the json file may contains the question's solutions, examples, questions only and concepts, the llm need to improvise the example solutions adding pedagogical aspect, solve the answers to the questions and include the concepts where required along.
v. dataset generation format:
		{
	  "question": "What is the value of the integral \\(\\int_0^1 x dx\\)?",
	  "answer": "The integral of x from 0 to 1 is (1/2)x^2 evaluated from 0 to 1, which gives (1/2)*1^2 - (1/2)*0^2 = 1/2. \\boxed{\\frac{1}{2}}",
	  "answer_plain": "1/2",
	  "topic": "calculus",
	  "difficulty": "easy"
	}


1. TESTING WITH DEEPSEEK-VL-TINY  MODEL for extraction instead, test if it works otherwise need a change in the approach or just replace the pdf file. search for other sources for dataset collection. 
2. Found two other maths book pdf file which are actually pdf file rather than a scanned image, so any pdf extracter might  work, testing today.(successfully extracted the text from the pdf file downloaded from web which is purely a pdf file)
## Qwen3 Dataset Generation
*Compare the performance difference between the models with different parameters counts (Qwen3 family) with rest of the models, the stats is providded below. Provide a clear picture for effective understanding and learning tables, examples, comparision anything. how good are those benchmarks from the real world perspective and performance.*

Benchmarks include general knowledge assessment (MMLU variants), graduate-level question answering (GPQA), math and STEM problem solving (GSM8K, MATH), coding skills (EvalPlus, MBPP), and multilingual capabilities (MGSM, INCLUDE).

considered models
Qwen3-30B-A3B (3b activated parameters,MoE model), Qwen3-14B(dense model better than phttps://huggingface.co/Qwen/Qwen2.5-VL-7B-Instructrevious 2.5 version),

**Desiderata"** is a plural noun derived from Latin, meaning **"things that are desired or needed."**
	- _The desiderata for a successful project include clear communication, adequate funding, and skilled personnel.
###################################################################

##  Bench marking and Testing Models for AI-Math
benchmarks the selective models on evaluation dataset crafted using the questions from Nepali curriculum math books and past questions. 

How to collect?

extract question with latex extractor,
create question answer pairs using some big model and verify its correctness.
benchmarks how many did the model got correct?
additionally keep remember adding reflective learning with  the model.

## evaluation dataset collection

<<<<<<< HEAD
**01-ai/Yi-1.5-34B-32K**  model fits within the resources of our pc, which will be used for generating the answers for extracted maths questions from the nepalese curriculum. 
the generated answers will be set as the correct labels for evaluating the maths-model for benchmarking on the actual real world dataset. 



*if a gguf model is of size 36gb and the system have 24gb of vram, 64gb or ram how will the ollama will utilizes the resources.*

VRAM will be utilized for accelerating the model inference along with the CPU offloading for required additional memory (RAM).



a python script that loads visual  langugage model qwen2.5-vl-3b-instruct,  this model should be able to loaded using ollama, 
(ollama run hf.co/unsloth/Qwen2.5-VL-3B-Instruct-GGUF:Q8_0)
the pdf file will be passed and every pages needs conversion to image and then extraction from that  image. 
code   should be minimalist, free from unnecessary comments line after  line, instead comments should explain how the parameters or any part of code is being used internally or in simple way. 
this is how i intend to run  the python file: python extract.py --file questions.pdf --prompt "extract all the questions from the provided image/pdf file(after pdf pages are converted to image)" 
simply convert each page in the pdf to an image then submit it llm asking it to convert to markdown preserving tables, lists, headers, symbols and mathematics language etc. then combine all the markdown back into the final document

## evaluation pipeline

**now that the extraction with mineru, preprocessing with 14b-qwen3b and answer generation with qwen3:8b is done, need to add one more aspect which allow checking the answer correctness with a bigger model (32b parameter qwen maybe) and this whole flow needs to be developed into a integrated pipeline, which takes a pdf, extract, preprocess, generate answers and evaluate the correctness of the answer with better/bigger model.**

#### process

Base64 is a way of encoding arbitrary binary data (like an image file’s raw bytes) into plain ASCII text, so that it can safely travel through systems that only expect text (for example, JSON payloads or email bodies).

but does the conversion to base64 actually keeps the content from the pdf file intact? does the visual language model like qwen2.5-vl-3b model directly takes the  png file or am i confused regarding this?
ans: Base64 is reversible and lossless, why do it? (Because JSON (or many HTTP clients) only handle text)
**Model input** is always numeric tensors—whether you fed them from a local PIL image or the server decoded them for you.


############
[mineru](https://opendatalab.github.io/MinerU/usage/quick_usage/#advanced-usage-via-api-webui-sglang-clientserver) pdf/image to text extractor advance extraction tool based on  paddleOCR accelerated using sglang backend
, later the extracted text is passed to llm like qwen3:8b to create json format questions sets from this corpus:

 mineru -p class-9-qp.pdf -o output_mineru: this gave absolutely amazing results a json file exactly I wanted. need preprocessing with a llm now to create benchmark questions.
 


gemini is good at creating such questions answer pairs, kimi is better

AIzaSyD7ogKDnYk_KUnGslnfG4NJ-OAxd-5z2nA

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H 'X-goog-api-key: GEMINI_API_KEY' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'

check  cosine similarity between the existing json and the preprocessed to identify the changes or differences before/after.

### preprocessing prompt

'''*preprocess the content of the json file (the json file contain the extracted corpus from Nepal's mathematics past question papers). Preprocessing includes structuring the corpus into question_no, [topic_name][class_10] and questions in json format. During extraction of the text, some part of the questions might have not extracted, your  task is also to fill those missing pieces.* '''

comprehensive prompt is created from above reference prompt.

	Preprocessing Instructions
	
	The JSON file contains the extracted corpus from Nepal's mathematics past question papers. Your task is to preprocess this unstructured extracted data and structure it into a well-formatted JSON with the following fields for each question:
	
	- **question_no**: The question number (e.g., "Question 1", "Q2", etc.).
	- **topic_name**: The topic the question belongs to (e.g., "Algebra", "Geometry", etc.).
	- **class_10**: Indicate that the question is for Class 10.
	- **question**: The full question text. If parts of the question are missing due to extraction errors, fill in the missing pieces based on context.
	
	Please output the structured data as a JSON array of objects, for example:
	[
	  {
	    "question_no": "Question 1",
	    "topic_name": "Algebra",
	    "class_10": true,
	    "question": "Solve for x: 2x + 3 = 7."
	  },
	  ...
	]

### models to use for preprocessing

qwen3:14b-instruct, deepseek-math-7b-instruct, 


### chain-of-thought prompting: to "think aloud"

**Chain-of-thought prompting** is a technique in AI where instead of asking the model to directly provide the answer, you ask it to generate intermediate reasoning steps that lead to the answer. This mimics human step-by-step problem-solving and helps improve the model’s accuracy, especially for complex tasks like math, logic, or multi-step reasoning.



=======
1. extract the questions answers from the past papers
2. [minerU](https://github.com/opendatalab/MinerU) extracts the data from the pdf file in json format. 
3. the extracted json file is unstructured and unprocessed content. 
4. this unstructured and raw data needs preprocessing. the preprocessing will be done using a large language model (automation with a script)
5. 


##### models comparison
qwen2.5-7b and qwen3-8b as Nepali math question solving model bench-marking the performance difference.
According to the result provided from Perplexity AI (sourced arXiv papers, reddit discussion and Qwen official documentation and results,  qwen3-8b is better in terms of mathematical reasoning and problem-solving. trained dataset is larger in case of qwen3-8b model with larger token contexts. 

testing the deepseek math model [[[llama-server -hf unsloth/DeepSeek-R1-Distill-Qwen-7B-GGUF:Q8_0]]}, a promising deepseek model (rest of the description after testing the model and a benchmark itself with the evaluation dataset created.)

this model have input tokens limit of 128,000 and  output token limits of 32768.

### models  comparison

1. DeepSeek-R1-0528-Qwen3-8B is likely the best for Nepalese maths curriculum topics, excelling in advanced reasoning tasks like calculus and algebra.
2. Qwen/Qwen3-8B appears good but is outperformed by its distilled version, with less specific data available.
3. DeepSeek-R1-0528-Qwen3-8B and DeepSeek-R1-Distill-Qwen-7B seem best for advanced areas like calculus and analytic geometry
4. topics include algebra, trigonometry, calculus, conceptual problems, word problems, arithmetic, business mathematics, advanced calculus, analytic geometry, computational methods, vectors, mechanics, mathematics for economics and finance, number concepts and operations, and coordinate geometry.
5. this model ranked above among 4 different tested models: DeepSeek-R1-0528-Qwen3-8B
6. DeepSeek-R1-0528-Qwen3-8B and Qwen/Qwen3-8B likely have the longest context lengths at 131,072 tokens, while DeepSeek-R1-Distill-Llama-8B and DeepSeek-R1-Distill-Qwen-7B seem to have 32,768 tokens, which may limit longer tasks.



################

AI maths quiz generation along with answers and short explanation using a strong llm, the entire syllabus can fit within the system prompt, so far the system prompt for grade 11 has been prepared. The quiz will be generated beforehand along with a very short explanation, in production a smaller llm like qwen3 0.6b will be given the short explanation and question with answer to provide longer explanation along with a chat interface for the student


