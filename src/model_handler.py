import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

class ModelHandler:
    def __init__(self, model_name="meta-llama/Llama-2-7b-chat-hf"):
        """Initialize and load the model on GPU if available."""
        print(f"[INFO] Loading model: {model_name} ...")
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            load_in_4bit=True,
            device_map="auto"
        )


        self.pipeline = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_length=512,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.1
        )

    def generate_response(self, prompt: str, history: str = "") -> str:
        """Generate a chatbot response from prompt + optional history."""
        full_prompt = f"{history}\n{prompt}" if history else prompt
        outputs = self.pipeline(full_prompt, pad_token_id=self.tokenizer.eos_token_id)
        return outputs[0]['generated_text']



if __name__ == "__main__":
    # Quick test
    mh = ModelHandler()
    print(mh.generate_response("Hello, how are you?"))
