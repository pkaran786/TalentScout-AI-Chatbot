def check_exit_command(user_input: str) -> bool:
    """Check if the user wants to end the conversation."""
    exit_keywords = ["bye", "exit", "quit", "goodbye"]
    return any(word in user_input.lower() for word in exit_keywords)

def fallback_response():
    """Default fallback message when chatbot doesn't understand."""
    return "I'm sorry, I didn’t quite understand that. Could you please rephrase?"
