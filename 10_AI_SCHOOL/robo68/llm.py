# llm.py
"""
Llama-cpp LLM wrapper for Phi-3 model.
Loads a quantized GGUF model (e.g. Phi-3 mini) and performs text completion.
"""

from llama_cpp import Llama

class LLMPhi3Mini:
    def __init__(self, model_path: str):
        """
        Initialize the LLM model.
        :param model_path: Path to the GGUF model file (quantized Phi-3).
        """
        self.llm = Llama(model_path=model_path)
    
    def generate(self, prompt: str, max_tokens: int = 128, stop: list = None, echo: bool = False) -> str:
        """
        Generate text completion for the given prompt.
        Returns the generated text (first choice).
        """
        response = self.llm(prompt, max_tokens=max_tokens, stop=stop, echo=echo)
        # The response is a dict; get the generated text of the first choice.
        choices = response.get("choices", [])
        if choices:
            return choices[0].get("text", "")
        return ""

# Example usage:
# llm = LLMPhi3Mini(model_path="phi3-mini-q4_0.gguf")
# answer = llm.generate("Q: What is the capital of France? A:", max_tokens=10, stop=["\n"])
# print(answer)
