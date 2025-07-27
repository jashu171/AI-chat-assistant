from transformers import AutoModelForCausalLM, AutoTokenizer
import kagglehub

class QwenChatbot:
    """
    A simple chatbot using the Qwen 0.6B model via HuggingFace Transformers and KaggleHub.
    """

    def __init__(self):
        """
        Initializes the chatbot model and tokenizer.
        """
        model_path = kagglehub.model_download("qwen-lm/qwen-3/transformers/0.6b")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_path)
        self.history = []

    def generate_response(self, user_input: str) -> str:
        """
        Generates a chatbot response to the user input.

        Args:
            user_input (str): The input message from the user.

        Returns:
            str: The chatbot's response.
        """
        user_input = user_input.strip()
        if not user_input:
            return "Please enter a valid message."

        # Prepare the conversation history
        messages = self.history + [{"role": "user", "content": user_input}]
        prompt_text = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

        # Tokenize and generate response
        inputs = self.tokenizer(prompt_text, return_tensors="pt")
        response_ids = self.model.generate(**inputs, max_new_tokens=512)[0][len(inputs.input_ids):].tolist()
        response = self.tokenizer.decode(response_ids, skip_special_tokens=True).strip()

        # Save to history
        self.history.extend([
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": response}
        ])

        return response

    def reset_history(self):
        """
        Clears the conversation history.
        """
        self.history = []