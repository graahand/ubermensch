[[openweights vlm (molmo and pixmo).pdf]]

1. so ranjay krishna ko lab le chai ekdam transparent vision language model banayeko xah not only model but the datasets as well. ani yo models haru ko unique and most important feature vanekai yesko dataset ho. khasma chai dataset banaune belama llm or vlm ko lagi k garinxa vanda OpenAI ko api or aru kunai Claude, Gemini jasto models haru batw dataset prepare garinxa bulk ma ani tyo synthetic dataset ma chai model lai train garinxa jasle garda k samasya aayo vanda, tyo dataset batw train gareko model open source vaye pani just tyo model tyo proprietary model ko distilled version matra hunxa tyo vanda badi kei pani garna sakdaina, especially vision language model ko case ma. 
2. So yo Molmo and PixMo vanne paper ma chai uniharu le ekdam novel approach batw dataset banayeko xah vision language model ko lagi jun ekdam costly, ekdam resource intensive, ani quality maintain garna garo hunxa compared to llm ko dataset. so uniharu le ekdam highly detailed image captions vako dataset banayeko xah pre-training ko lagi, ani free-form image q&a dataset (vaneko rigid,fixed caption navayerw explanable general and natural labels for the images are collected) ani innovative 2d pointing dataset (vaneko objects haru point garna ko lagi localization pani garxa co-ordinates ko basis ma). yo sabai datasets kunai pani external vlms use nagari banayeko dataset ho. 
3. yiniharu ko best model 72b parameter ko jasle teti bela (5 dec 2024) ma proprietary vlms like claude 3.5 sonnet, gemini pro 1.5 jasto models haru lai academic benchmarks ma peldiyo ani gpt-4o sanga chai compettion ma second vayo. 
4. yo model chai sota model thiyo in their class of openness vaneko jasle sabai kura openly reproducible tarika le banauna khojxa tyo class ma otherwise properatary models haru sanga tw compete garnu garo hunxa. 
5. natural image understanding ani counting ma chai molmo specialized jo xah aru models haru vanda but advance reasoning problems haru ma chai properatary models haru le yeslai peldeko xah 
6. yiniharu ko dataset ma 712k image haru thioyo josma harek image ko lagi around 200+ words ko caption pani thiyo which wasn't annotated by the crowdsourcing plaform rathery they innovated something very useful technique. 
7. uniharu le annotators haru lai 60-90 seconds samma ko lagi image lai explain garna lagaye (speech ma) ani tyo explanation lai chai as the annotation use garyo. yesari first hand data collection ma modality change garne trick le ekdam  high quality dataset chai banauna help garyo without using any proprietary vlms.
8. Pixmo euta single dataset matrai haina esma arrays ko  dataset haru xa pre-training and finetuning ko lagi. instruction tuning dataset banauna ko lagi uni haru le users sanga batw interactive way ma free-form dataset collect garey for 72k images, annotations haru 162k thiyo (multiple annotations haru thiyo, euta visual object ko barema different comments (free-form annotation))
9. ani uniharu le language rw image lai grounding garna ko lagi 2.3 million grounding annotations haru liye  images(223,000 images) haru batw, uni haru le bounding box(rectangle) or segmentation mask ko thauma just (x,y) single points use garey jasle garda annotation pani ekdam past ani feasible vayo ani counting, identification jasto tasks haru ko lagi yesle majjale kaam pani garne vayo. 
10. The system uses a clever HTML-like format where coordinates are scaled from 0-100 regardless of image size: `<point x="10.0" y="10.0" alt="Mt. Rainier">mountain</point>`. This makes the system resolution-agnostic - works the same whether the image is 100x100 pixels or 4K.
11. they specifically generated the synthetic dataset tarw kunai vlm use nagari just llm use garerw code generate garyo ani specifically (clock reading, chart understanding ani table understanding ) jasto tasks haru ko lagi chai recipe jasto synthetic dataset banayo, like instead of learning about wine by tasting it, they studied chemical formula of the wine. 
12. uniharu le model train garne tarika pani ekdam innovative and effective thiyo jaha uniharu le pre-trained llm ani vision encoder jo use gareko thiye just like any other vlm but special kura k thiyo vanda uniharu le two stage training pipeline banayo  (three stage hunxa jaha connector  tuning garinxa jasko matlab chai noisy data ma structure find garna ko lagi llm lai train garne kura ho if dataset ramro xaina vane), novel overlapping multi-crop strategy use garyo (yesle chai instead of image lai grid grid garerw slide garne thauma esle chai overlapping grids haru banayo jasle garda context samjhinu parena grid grid garerw image lai read garda, crop ko boundaries ma hune information loss rokyo yesle), ani efficient multi-annotation learning (yesko matlab euta image ko multiple annotations xah vane pani training ekaichoti hune vayo instead of creating duplicate image ani tyo image ko different different captions), ani vision/language connector lai pani improve garyo (the vision-language connector bridges visual and textual understanding in multimodal AI. Traditional methods use basic feature stacking. Molmo employs attention-based pooling that preserves spatial relationships effectively. This technical innovation significantly enhances performance on visual reasoning and counting tasks.)
13. 

## sep 23

1. **Special note:** This isn't just concatenation - the attention masking creates isolated "training universes" within one sequence. It's like having three separate conversations happening in soundproof booths all facing the same painting.
   ![[molmo-img-processing-flow.png]]
2. 


##### DIFFERENT KIND OF VIEWS
1. BIRD VIEW (LOW RES)
2. GROUND VIEW (MEDIUM RES)
3. CLOSE-UP VIEW (HIGH-RES)


## Molmo Model Parameters 
### Image Encoder 
converts images into data the model understands. 

| Parameter Name | Value     | What does  it does?                                                                    |
| -------------- | --------- | -------------------------------------------------------------------------------------- |
| Params         | 290m-310m | number of trainable weights/parameters where large models capture more visual details. |
| Dim            | 1024      | feature dimension for visual processing, same across models.                           |
| MLP Dim        | 4096      |                                                                                        |
| Activation     | GELU      |                                                                                        |
| Heads          | 16        | parallel attention heads                                                               |
| KV Heads       | 16        | key-value attention heads                                                              |
| Layers         | 23        |                                                                                        |
| Image Size     | 336 x 336 |                                                                                        |
| Patch Size     | 14        |                                                                                        |
| Dropout        | 0.0       |                                                                                        |

### VLM Connector
links visual understanding with language capabilities.


| Parameter Name | Value      | What does it does?                                                                                |
| -------------- | ---------- | ------------------------------------------------------------------------------------------------- |
| params         | 12m-310mm  | connector size grows with model scale (bigger the model, bigger the vlm parameters count as well) |
| pool size      | 2x2        | 2x2 matrix grouped for pooling (like summarizing)                                                 |
| pool dim       | 1024       |                                                                                                   |
| pool heads     | 16         |                                                                                                   |
| MLP Dim        | 1024-59136 |                                                                                                   |
| Activation     | SwiGLU     |                                                                                                   |
| Dropout        | 0.0        |                                                                                                   |


### LLM
language understanding component. 


| Parameter Name | Value         | What does it does?                                                 |
| -------------- | ------------- | ------------------------------------------------------------------ |
| params         | 1.2b-72b      | 1b-e is for moe model                                              |
| embed          | 50304-152064  | vocabulary size for language embedding                             |
| dim            | 2048-8192     | langauge feature dimension                                         |
| mlp dim        | 2048x64-59136 |                                                                    |
| activation     | SwiGLU        |                                                                    |
| Heads          | 16-80         | attention heads                                                    |
| KV heads       | 4-8           | relatively small for language model as comapred to vision encoder. |
| layers         | 16-64         |                                                                    |
| theta          | 10k-1m        | positional encoding range for handling longer sequences.           |
| dropout        | 0.1           | small dropout only in llm                                          |

### Pre-training
initial training on image caption pairs. 


| Parameter Name | Value        | It does what?                                            |
| -------------- | ------------ | -------------------------------------------------------- |
| Warmup steps   | 2000         | gradual learning rate increase                           |
| Learning rate  | 2e-5 to 6e-6 | lr decreases for larger models because they learns fast. |
| cosine delay   | 10%          |                                                          |
| eps            | 1e-6         | prevents division error during trainining                |
| betas          | 0.9, 0.95    | momentum parametes for optimizer stability               |
| batch size     | 128          |                                                          |
| steps          | 22.3k        | total training iterations.                               |

### Finetuning
specialized trainign for specific tasks.

| Parameter Name | Value        | it does what? |
| -------------- | ------------ | ------------- |
| warmup steps   | 2000         |               |
| Learning rate  | 5e-6 to 3e-6 |               |
| cosine decay   | 10%          |               |
| epsilon        | 1e-6         |               |
| betas          | 0.9, 0.95    |               |
| batch size     | 256          |               |
| steps          | 20k-32k      |               |

A RESEARCH PAPER ONE AFTER ANOTHER WILL BE UPLOADED IN THIS CHAT, AND THEN SPECIFIC PARTS FROM THE PAPER, DIFFERENT QUESTIONS RELATED TO THE PAPER NEEDS TO BE DONE BY YOU. THE EXPLANATION MUSTN'T BE VERY LENGTHY RATHER IT SHOULD BE A STORYTELLING (NO EMOJIS ALLOWED) EXPLANATION YOU MAKE IT CLEAR BY PROVIDING ANALOGIES, EXAMPLES, SCENARIOS, SPECIAL NOTES, ALERT NOTES, INSIDER NOTE MAYBE ANYTHING THAT WILL HELP TO UNDERSTAND THAT TOPIC OR CONCEPT WITH CONTEXT. 

RESPOND WITH YES IF YOU UNDERSTAND THIS TASK.