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

question answering is primary feature for this project but integration of pedagogy enhanced with AI is another feature. Such pedagogical philosophy for reflective and effective digital learning  is the main focus of mysecondteacher platform. This philosophy can be hugely impacted with the integration of efficient large language models along with AI assisted reflective and effective learning can be sun ma suganda. 

can we integrate the llms with the content of mysecondteacher videos lessons? students learns from video sessions and communicate with llms at the same time? this can be absolutely groundbreaking. 

# dataset development

start with maths dataset, class four content, dataset development automated through a llm where a book is provided as a file performing Retrieval Augmented Generation for generating the questions-answer pairs along with important concepts and pedagogical and reflective learning emphasized. 

pdf reader package from python or any OCR technology for correct extraction of the text for vectorization and ......

key consideration: to preserve the way mathematics is expressed and solved unlike language subjects, we need to keep the symbols, flow, concepts intact for quality d

####################################
AI MATH EDUCATION – 90-DAY SPRINT PLAN

(1 dataset → 1 model → 1 evaluation, language subjects first)

Phase 0  (Week 0) – Project Skeleton  
• Git repo: `mst-nepali-llm/` with folders `data/`, `models/`, `eval/`, `infra/`  
• Decide hardware budget:  
  – 1 × RTX 4090 24 GB (local PC) for 7-8 B fine-tunes  
  – Google-Colab-Pro+ vouchers (≈ 100 H100-minutes / month) for bigger runs  
• Tooling lock-in: PyTorch 2.2, transformers 4.40, xtuner 0.1.20, unsloth 2024.5, llama.cpp+vLLM.



-------------------------------------------------
Phase 1 – NEPALI LANGUAGE MODEL  (Weeks 1-4)
1. Dataset (single JSONL)  
   • 5 k CDC Nepali textbook Q-A pairs (manual scrape)  
   • 2 k grammar-rule examples w/ explanations  
   • 1 k creative-writing prompts + graded samples  
   • 500 synthetic dialogues (translate Alpaca-Nepali, then manual QA)  
   → Final 9 k rows, tokenised 2 M tokens. 80/10/10 split.

2. Base model choice  
   • OPENWiseyak-7B (Nepali continual-pretrained Llama-3) – already fits 24 GB VRAM.  
   • If memory tight → 4-bit QLoRA (r=64, α=128, 4-bit NF4).

3. Fine-tune on local PC  
   ```
   xtuner train configs/nepali_qlora.py --deepspeed zero2
   ```
   3 epochs, 30 min / epoch on 4090.

4. Evaluation  
   • Rouge-L ≥ 0.55 vs reference answers  
   • Pedagogical rubric: clarity, grade-level vocabulary, cultural context.  
   • Export GGUF → llama.cpp server (4-bit) → latency 120 ms / 512 tokens.

-------------------------------------------------
Phase 2 – SOCIAL STUDIES  (Weeks 5-8)  
Same pattern: scrape 6 k CDC Q-A, 1 k map-based short-answer, 500 essay samples.  
Fine-tune Nepali model with LoRA adapters (`--adapter_path social_lora`).  
Merge adapters for single multi-subject checkpoint if VRAM allows.

-------------------------------------------------
Phase 3 – ENGLISH  (Weeks 9-12)  
Reuse Llama-3-8B-Instruct, add 7 k English-Nepali parallel grammar+writing samples.  
Switch to vLLM backend for higher throughput (≈ 500 req/s on 1×4090).

-------------------------------------------------
Phase 4 – MATH & OPTIONAL MATH  (Weeks 13-18)  
1. Dataset  
   • 8 k CDC Class-4-12 math problems (incl. optional)  
   • Each row: problem, step-by-step solution, final answer, concept tag.  
   • Geometry: 1 k diagrams + LaTeX captions (render diagrams → base64).  
   • Sets: 500 word-problems → formal notation.

2. Model strategy  
   • Base: **DeepSeek-Math-7B** (reasoning-oriented, 30 % smaller than Llama-3-8B).  
   • Full fine-tune 1 epoch on Colab H100 (mixed-precision fp16).  
   • 4-bit GGUF post-train for on-prem.

3. Evaluation  
   • Exact-match accuracy ≥ 70 % on unseen CDC questions.  
   • Step-level correctness judged by Sympy verification.

-------------------------------------------------
Phase 5 – SCIENCE  (Weeks 19-24)  
Same pipeline; include 5 k Q-A, 1 k experiment explanations.  
Use multi-modal adapter to reference diagrams (clip-interrogator for images).

-------------------------------------------------
Integration with MySecondTeacher Videos  
• Add transcript-time-aligned JSON to each video lesson.  
• vLLM endpoint receives: `{"video_id": "ss_8_3", "timestamp": 123, "student_query": "..."}`  
• Prompt pattern:  
  ```
  <context>Video transcript: {transcript_snippet}</context>
  <question>{student_query}</question>
  <instruction>Answer in Nepali, cite timestamp, give follow-up question.</instruction>
  ```
→ Grounded chatbot inside MST web player.

Pedagogy Hooks  
• Reflection prompt after every 3 interactions: “What did you learn from this exchange?”  
• Store reflections in local SQLite; nightly aggregate → teacher dashboard.

-------------------------------------------------
Resource & Cost Reality Check  
• Local PC electricity ≈ $3/week.  
• Colab-Pro+ monthly ≈ $50 (self-funded).  
• All checkpoints < 20 GB; push to HuggingFace private repo for backup.

Deliverable at end of 24 weeks:  
Five LoRA adapters + merged 7-8 B multilingual checkpoint, llama.cpp+vLLM serving scripts, and API contract for MST frontend.