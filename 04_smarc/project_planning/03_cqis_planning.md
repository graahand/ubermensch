#smarc #rnd 
# Central Quality Inspection System

this system is aims to identify design flaws using AI


aspect ratio (ratio of height and width): done ()
resolution (number of pixels in width and height): no problem ()
logo placement (WORKING A4)
text/typo (text extract)
blur detection (dekhauna layek)

margin(space between the image/design edge and the last elements closest to the edge of the image/design)


text, typos and grammar (text extraction is done first with doctr(document text recognition)) and as expected it didn't worked well out of the box and needs preprocessing which isn't feasible at all keeping in mind that the designs can be of any types (creativity, subjective)

color code for web usage and print usage (cmyk and rgb, no problem)

### needs to be done

1. font checker (different ING colleges have different fonts they use, apex and kavya have different primary font, rest of the ing's colleges primary font and typeface is roboto) also there are numerous secondary fonts for each colleges. (when to use primary font, when to use secondary font?)

2. logo placement works or not? (not known)

3. blur detection (can it be done with any vision language model guided with appropriate prompt.) needs an experimentation. 

4. if the algorithms or models are not working properly for text extraction, here also vision language model can rescue (i already worked on such project where vlm (moondream2 and qwen-vl-3b/7b) is used for text extraction (fyp))


5. a guidelines report is essential (kimi_ai allow 50 files upload, uploading the files shared from icreate to write down the actual guidelines)

6. font confirmation

7. typos and grammar mistakes (gramformer, pyaspeller, python-language-tools, )



1. logo 



finetuning vlm with all the information about the guidelines. 

how to finetune??

dataset should contain following: 
    design image
    what text is written? exact
    what font is used? 
    does it contain any unwanted blur or not?
    logo placement correct or not? 
    check whether the design templates are not distorted, cropped or scaled differently or oddly? 
    

## experimentation 1

without finetuning and careful prompting, text extraction can be done, font classification is only possible with a trained CNN. logo placement done through algorithm and pre-defined criteria. 

**model usage** [[05_ai_maths#How ollama uses the model such that they can run easily on consumer hardware?]]

segmentation of any use? for blur detection?? 


## Information to be extracted from the shared CQIS folder

1. primary and secondary fonts/typeface of each ing college.
2. Logo placement guide for A4, A3, A5,digital collaterals (margins), color theme and do/don't regarding the logo (text color, background color) 
3. story guide (consult to niraj dai , what does story means? is it social media story? if yes then write down the criteria in words)
4. write down the criteria for standees (every ING colleges) like margin and logo placement and any other essential details. 


5. Dataset format for vision language model: 
    a. design template/image
    b. which typeface used (primary and secondary)
    c. what text is written in the image and is it correct (typos/grammar)? any text overflow or weird line breaks inside the designs. 
    d. any distorted, pixelated or unnecessarily/mistakenly blurred region in the image
    e. logo placement and margin for A4, A3, A5, digital collaterals, social media cover pages and standee (30x72)
    f. color guidelines (logos, background, text color)

inclusion of positive cases and negative cases in dataset and requires minimal human intervention.


    image_id:01,
    image_path: img.png,
    typeface used: roboto, (can model learn to identify?)
    blur/pixelated_regions_present: yes (co-ordinates)/no, (can model learn)
    text_written: islington college, congratulations graduates!!, 
    grammar check: positive/negative,
    logo_placement: co-ordinates() (can model extract accurately) 
    logo_margin: 30px (can model learn?) 
    type_of_templates:A4/A3/A5 (i don't know whether the model can learn to identify size of template), 
    logo_color_check: positive/negative
    logo_background_check: positive/negative


##  can a vision language model like qwen can learn these things after finetuning? if  yes then how many positive and negative samples required, help me with the data collection and preparation.?


### convolutional neural network for typeface classification

data collection by generating the typeface/font text to image from font file like  .ttf or .otf which are easily available.

generate the images using using openly available tool/model that can be run with  the resources from our pc. 

real world samples will be very valuable.

required samples for each typeface is at least 1000. 

here is the link to the dataset which needs some exploration and can be useful for this task. its a font recognition dataset by Adobe. train data is around 18gb with 2383 font classes. pretrained model is DeepFont produced along with the dataset by adobe research. 

feasiblity and initial reports required fast. 

for now research on vlms is on hold. 
(https://www.kaggle.com/datasets/luisgoncalo/adobe-visual-font-recognition?select=train.bcf)





#############################################################

## improvement

college specific words that are correct but flagged as incorrect like pokhara university for apex college, BSc(hons) computing for islington college, and so on
such words shouldn't be marked as incorrect. 

##########################

## CQIS Meeting minutes July 20, 2025

font detection works mildly, 
color palette also works mildly,
logo placement check for every sizes, not perfect,
text extraction and grammar checking working  fine, 
allowed words setting by the admin for different organization mildly working, 
white space checker also working,
pix-elated images not working,(laplacian, decimation difference, edge detection consistency, frequency domain analysis, gradient magnitude statistics, superpixel segmentation(clusters of similar neighbouring pixels, blurred regions have low texture variance and weak edges due to smoothing which can ), )

what should be done next?
**font detection, color palette, logo placement, blurred out images existing condition and improvement planning**

**action plan for those improvements, what discussed, deadlines set for planned actions.** 

1. production ma gako xaina (feedback)
2. color palette detection(only extracts the colors, doesn't check the actual placement)
3. blur detection (not today)
4. allowed words. 
5. standee add garnu (criteria)
6. 

a python script that uses vision language model to extract the dataset in json format, the extracted text should be in latex format 
#################################################################

BURN (RUST NN LIBRARY)



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


#### process

Base64 is a way of encoding arbitrary binary data (like an image file’s raw bytes) into plain ASCII text, so that it can safely travel through systems that only expect text (for example, JSON payloads or email bodies).

but does the conversion to base64 actually keeps the content from the pdf file intact? does the visual language model like qwen2.5-vl-3b model directly takes the  png file or am i confused regarding this?
ans: Base64 is reversible and lossless, why do it? (Because JSON (or many HTTP clients) only handle text)
**Model input** is always numeric tensors—whether you fed them from a local PIL image or the server decoded them for you.


###
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

*preprocess the content of the json file and include question only along with adding class10 and topic name [class10][topic_name].  if any missing text, part or question found then fill it contextually.* 

this prompt will generate tthe type of dataset i want.


1. extracted the past question papers from class4-class12 maths, one past paper or model question paper for each class. 















