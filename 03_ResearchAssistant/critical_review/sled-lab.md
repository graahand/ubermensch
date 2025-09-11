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
14. 

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