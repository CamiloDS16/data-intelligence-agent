from abc import ABC, abstractmethod

class LLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Take a prompt, return generated text"""

class OllamaProvider(LLMProvider):
    def __init__(self, model: str = "llama3.2"):
        self.model = model

    def generate(self, prompt: str) -> str:
        import ollama  
        response = ollama.chat(
            model = self.model,
            messages = [{"role": "user",
                         "content": prompt
            }],
        )

        print(response)
        return response["message"]["content"]
    

if __name__ == "__main__":
    # test
    print("--- Running tests manually ---")
    agentic = OllamaProvider()
    print(agentic.generate("Say hello in fashionable way"))

    