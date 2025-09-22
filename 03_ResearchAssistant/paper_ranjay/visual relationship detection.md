[[visual-relationship-detection.pdf]]

1. this papers basically have two different aspects, language aspect and visual aspect. 
2. This paper introduces a model for visual relationship detection that learns object (noun) and predicate (verb or adjective) appearances separately (O(N+K) detectors) instead of full relationships (O(N²K)). It leverages language priors (language understanding and semantics) from word embeddings to detect rare/unseen relationships (between objects), enabling zero-shot learning and improving image retrieval performance.
3. RCNN is used for object's proposal. 
4. The paper evaluates visual relationship detection using Recall@100/50 metrics across three conditions: predicate detection (predict relationships given objects), phrase detection (label relationship regions), and relationship detection (find objects AND relationships). mAP isn't used as it penalizes correct but unannotated relationships. With 70 predicates and ~18 objects/image, random guessing would yield only 0.00014 Recall@100. The authors compare their model against state-of-the-art approaches through ablation studies.
5. 
6. Imagine teaching someone to understand grocery photos. Instead of showing every specific pairing ("milk next to cereal"), teach:

	1. **Individual items** (milk, cereal, bread)
	2. **Relationships** (next to, on top of, inside)

	Add **language knowledge**: "Milk" and "juice" are similar (both drinks), so if they've seen "milk next to cereal" but never "juice next to cereal," they can guess what it looks like.
	
	When searching for "eggs inside carton," the system finds exact matches—not just images with eggs AND cartons separately. Just like you'd understand "soda inside fridge" even if you've only seen "milk inside fridge" before!

7. Imagine teaching someone photo composition. Instead of showing every specific pairing ("mountain behind lake"), teach:

	1. **Individual elements** (mountains, lakes, trees)
	2. **Relationships** (behind, next to, reflecting)

	Add **composition knowledge**: "Mountains" and "hills" are similar, so if they've seen "mountain behind lake" but never "hill behind lake," they can guess what it looks like.
	
	When searching for "sunset over ocean," the system finds exact matches—not just images with suns AND oceans. Like understanding "moon over ocean" even if you've only seen "sun over ocean" before!\
8. 