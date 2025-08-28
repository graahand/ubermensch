
#llm 
#rnd 
## first impression of the model 

**Goal:** Understand the model’s “personality” and basic behavior.

- Ask **warm-up conversational questions**:
    
    1. “Hello! How are you feeling today?”
        
    2. “Describe yourself in one sentence.”
        
    3. “What do you think you’re good at?”
        
    4. “Tell me a short, funny joke.”
        
- Observe:
    
    - Is it polite, friendly, robotic, or overly formal?
        
    - Does it admit limitations?
        
    - Does it feel _human-like_ or obviously scripted?
        

	 Log example:

> _Friendly tone, but repeats disclaimers often. Humor feels generic. Gives short but coherent self-description._

## reasoning and problem solving

**Goal:** Check logical thinking and chain-of-thought style (without needing internal reasoning).

- **Prompts to try**:
    
    1. “If I have 5 apples and I eat 2, then buy 7 more, how many do I have?”
        
    2. “You see a boat filled with people. It hasn’t sunk, but when you look again you don’t see a single person on the boat. Why?” (classic riddle)
        
    3. “Explain why the sky is blue in simple terms for a 7-year-old.”
        
- Observe:
    
    - Does it explain _step-by-step_ or just give final answer?
        
    - Can it catch riddles/trick questions?
        
    - Is reasoning sound or flawed?
## factual knowledge check 

**Goal:** See if it can retrieve and express factual info without hallucination.

- **Prompts to try**:
    
    1. “Who is the current president of Nepal?” _(Expect hallucination if model is not updated — check how it handles outdated info.)_
        
    2. “Name 3 moons of Jupiter.”
        
    3. “Explain what CRISPR does in genetics.”
        
- Observe:
    
    - Does it admit uncertainty or fake answers?
        
    - Does it mix correct and wrong info?
        
    - Is language precise or vague?

## Creativity and Open-Ended Generation
**Goal:** Measure imagination, narrative flow, and flexibility.

- **Prompts to try**:
    
    1. “Write a short bedtime story about a robot who learns to cook.”
        
    2. “Create a poem about AI in the style of Shakespeare.”
        
    3. “Invent a fictional technology and explain how it works.”
        
- Observe:
    
    - Is it original or generic?
        
    - Can it adapt to tone/style requests?
        
    - Does it make sense while being creative?
## Follow up and Context Retention

**Goal:** Test how well it remembers prior conversation.

- Example flow:
    
    1. Ask: “My name is Vivek. Remember that.”
        
    2. Later: “What’s my name?”
        
    3. Give it a task requiring multiple steps and refer to earlier parts.
        
- Observe:
    
    - Can it connect back to earlier answers?
        
    - Does it lose context quickly?
        
    - Does it self-contradict?

## Final Notes

Model Name:  
Model Size:
Quantization_scheme: 
License: 
Date Tested:  
Version / Source:  
Strengths:  
Weaknesses:  
Best Use Cases:  
Not Suitable For:  
Overall Feel: 