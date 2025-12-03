#ra 
1. a lab working on vision language model from university of michigan. their most famous and influential paper is about grounding the llm or vlm. (connecting language units to their referents in the phyical world is grounding)  

2. grounding open vocabulary acquisition (GOVA) is a process josma next word predict garne vanda ni words haru ko real world meaning lai visual information ko through associate garxa. like manxe le physical interaction batw language sikne garxa.

3. vision language models haru ma GOVA le model train garda next word predict sang sangai use vako words haru lai visually physical world ma image ko through ground garxa or justify garxa. 

4. sled lab le afno world-to-words:grounded open vocabulary acquisition vanne paper ACL 2023 ma publish gareko thiyo rw yo paper ma mention vako model chai [OctoBERT](https://huggingface.co/sled-umich/OctoBERT) ho.
5. referential grounding vaneko chai language units (cat) lai tesko physical world referents sanga connect garnu ho josle garda kunai pani words ko grounded meanings haru learn and understand garna important role khelxa. 
6. aru VLMs ko comparision ma OctoBERT le grounding chai pre-training ko time ma sikxa ani tyo sikeko kura lai transfer garerw unseen words haru sikna ko lagi use garxa without any grounded supervision. Pre-training ko belama OctoBERT le 3ta kaam garxa: masked language modelling, object localization and grounding through word-region alignment(ensure model connects the words to their corresponding objects in the image).
7. cloze_test vaneko fill in the blanks wala test hai tw. 
8. Yo world-to-words vanne paper ma grounded vlm ko lagi duita new evaluation metrics proposed gareko xah grounded hit rate (G-HR@k) and grounded perplexity (G-PPL).
9. grouned  hit rate le chai language modelling ani object detection combine garxa and measures whether the predicted word (top_k vaneko top guesses haru) is correct and the bounding box created have IoU over 0.5. 
10. ani G-PPL le chai perplexity score adjust garxa model ko on the basis of how well model identifes the object's location, if IoU zero xah vane G-PPL very high hunxa, if IoU 0.8 vanda mathi xah vane chai G-PPL adjust garerw lower hunxa which relfects the correctness in both word prediction and object localization. 
11. yo paper ma pahila pre-training ko belama model le naya words haru sikxa (base words), tespaxi few-shot learning ma chai language batw chai context nikalxa like (this is a [mask]) ani visual information image dekhi nikalxa tespaxi prediction garxa (prediction vaneko chai association ho visual entity ani tyo missing word ko bichma)
12. incremental class learning vaneko chai naya objects haru siknu without forgetting something that have learnt before. 
13. yo paper le Flicker30k dataset use gareko xah pre-training ko lagi with additional curation. 
14. OctoBERT model ko architecture ko kura garda chai, yesle chai pre-trained language model ani CNN use garxa text rw image ko relationship bujhna ko lagi. dual-stream vlm (text ani images), yo duita modalities haru respective encoder le encode garisakepaxi euta common format ma convert garixa ani tyo combine gareko text-image representations lai cross-encoder le self-attention mechanism ko lagi use garxa.tespaxi cross-encoder batw aayeko output lai object decoder ma pass garinxa jasle image batw objects haru context anusar identify garxa, tespaxi finally identify vako object ko basis ma text-decoder le language modelling garxa. 
15. yesko example vaneko, let's suppose a input text "a man is playing football" with a image of man playing football. the text is processed by pre-trained language model to understand its meaning, tespaxi cnn le image batw objects and features extract garxa. tyo text rw image representation common format ma convert garerw combine hunxa, tespaxi cross-encoder le tyo combined information porcess garerw object decoder lai pathauxa  jasle object identify garxa (man and football) using the object queries and finally yesle text understanding rw generation chai improve garne vayo. 


## qwen3 dense
1. Think of this like a dictionary with 151,000 entries — every word or piece of word it can understand: what if any word other than these 151,000 words that the model knows?
2. what about qk-norm? absolute positional embedding, NoPE as well right? so how the rotary differ and actual what does that rotation means? any example or analogy?
3. it adjusts the scale of activations without shifting them.: what does this means? shifting them? how does this RMSNorm actually works in one liner tell me. 
4. This helps the model learn complex patterns; i never understood the feed forward network inside of the transformer block, what is its purpose and how SiLU differ from ReLU, and how does the relationship/pattern is learnt here? on what input does this happens?
5. what about residual blocks there and the cross sign button between SiLU block and linear layer. 
6. gqa also calculates the attention score right? and what happens to this attention score?  
7. A **linear layer** that maps the high-dimensional representation back to the **vocabulary size (151k)**: a high-dimensional representation as in? what does this means and how they are mapped to vocabulary size of what actually mapping means here?
8. what about logits? are they also generated if yes then what generates them? 
9. This refers to the **size of the feed-forward network’s inner layer**.: what does the feed forward network's inner layer actually means this is too much confusing. where are they located actually?
10. also why many transformers blocks how does it actually works?
11. deeper models vs wider model architecture and what are the architectural choices that actually affects the number of parameters size. 


==yo sled lab ko professor chai joyce y chai ho, uslai contact garne ki?==
==yo labs ko important papers haru:==
1. ==world-to-words:grounded open vocabulary acquistion through fast mapping in Vision-Language-Models (2023)==
2. ==mindcraft:theory of mind modelling for situated dialogue in collaborative tasks (2021)==
3. ==beyond nombank: a study of implicit arguments for nominal predicates (2010)==
4. ==do visio language models represent space and how? evaluating spatial frame of reference under ambiguities (2025)==
5. ==3d-grand: a million scale dataset for 3d llms for better grounding and less hallicunation (2025)==
6. ==multi-object hallucination in vision-language models (2024)==
7. ==experience ground language (2020)==
8. ==seagull: an embodied agent for instruction following through situated dialog (2023)==
9. ==vision-and-language navigation today and tommorrow: a survey in era of foundation models.==
10. ==groundhog: grounding large language models to holistic segmentation.==