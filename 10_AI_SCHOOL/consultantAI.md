## Available models for korean language

1. Qwen3-4b (Highly efficient and SOTA model from alibaba and specially trained for conversational AI.) {tested}
2. IBM-Granite (Multilingual model from IBM, not tested yet!)
3. LFM2 (model with korean and english support, liquidAI, not tested yet!)
4. LFM2-1.2B-RAG (specialized model for RAG based usecases.)
5. LFM2-2.6B (tested, efficient and good choice)

> Note: Large language models specialised only for korean and english language can be found with good research, otherwise korean language spefic finetuning  is required for the model to be efficient for day to day conversation and the described use case by the client. 

## Steps

1. Choose a model
2. Test the model without finetuning with user interactions and real usecase (helps in requirement gathering,  how the model should respond) (At least 1 week of interaction with the model and the history of the interaction will be used to analyse the requirements.)
3. Databases and File integrated and retrieved by the model as a reference and improvising its default response (KEY FEATURE). 
4. Deployment [Xeon CPU based server with at least 32GB RAM](https://www.digitalocean.com/pricing/droplets#cpu-optimized) or GPU-providers like DigitalOcean, AWS, Google  Cloud Platform to get the [single H1000 GPU instances](https://cloud.digitalocean.com/registrations/new?activation_redirect=%2Fgpus%2Fnew%3Fsize%3Dgpu-rtx6000x1-48gb&redirect_url=%2Fgpus%2Fnew%3Fsize%3Dgpu-rtx6000x1-48gb). 
5. Model Size: Below 7B parameter (Above this size, GPU-based hosting will only work, CPU based servers won't work in this case and only work in case  of models smaller than 7b.)

> Note: Finetuning a model for this usecase is indeed very possible but the dataset development requires much more attention and manual effort as compared to the training process and training cost. So, the dataset development part must be considered seriously. 

## Project Pipeline

FrontEnd Chat UI (ReactJS) sends request (Text conversation) - API Endpoint takes the request to backend (Django, Node/ExpressJS) - Request converted to Python Data structure - Request (TEXT) sent to LLM hosted in GPU or CPU instance - LLM (think about the question and what the response should be [increase the response time, but  coherent responses are provided]) - LLM generates the response - Backend serves its via API - FrontEnd renders the response to the user. 

## Samples of conversations with Qwen3-4b

![[Pasted image 20251117224552.png]]
image_1


![[Pasted image 20251117224615.png]]
image_2



![[Pasted image 20251117225634.png]]
image_3



## Sample conversation with LFM2-3.6B model

![[Pasted image 20251117225816.png]]
image_1


![[Pasted image 20251117230119.png]]
image_2

![[Pasted image 20251117230311.png]]
image_3