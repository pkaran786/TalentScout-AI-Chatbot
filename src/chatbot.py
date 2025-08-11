# chatbot.py
from model_handler import ModelHandler
from prompt_engineering import (
    greeting_prompt, field_prompt, tech_stack_prompt,
    farewell_prompt
)
from data_handler import save_candidate_data
from utils import check_exit_command, fallback_response


class Chatbot:
    def __init__(self):
        self.model_handler = ModelHandler()
        self.candidate_data = {}
        self.state = "GREETING"
        self.fields = ["full_name", "email", "phone", "experience", "position", "location"]
        self.current_field_index = 0
        self.tech_list = []
        self.conversation_history = ""  # To maintain context

    def _add_to_history(self, role: str, text: str):
        """Add a message to conversation history."""
        self.conversation_history += f"{role}: {text}\n"

    def _move_to_next_field(self):
        """Advance to next candidate info field or tech stack phase."""
        self.current_field_index += 1
        if self.current_field_index >= len(self.fields):
            self.state = "TECH_STACK"
            return tech_stack_prompt()
        return field_prompt(self.fields[self.current_field_index])

    def process_input(self, user_input: str) -> str:
        """Process user input based on the conversation state."""
        user_input = user_input.strip()
        self._add_to_history("User", user_input)

        # Exit handling at any stage
        if check_exit_command(user_input):
            if self.candidate_data:  # save partial data if any
                save_candidate_data(self.candidate_data)
            self.state = "END"
            response = farewell_prompt()
            self._add_to_history("Bot", response)
            return response

        # GREETING STATE
        if self.state == "GREETING":
            self.state = "INFO"
            response = (
                "Hello! 👋 I'm TalentScout, your AI Hiring Assistant. "
                "I’ll start by collecting some basic information about you "
                "and then ask a few technical questions based on your tech stack.\n"
                + field_prompt(self.fields[self.current_field_index])
            )
            self._add_to_history("Bot", response)
            return response

        # INFO STATE
        elif self.state == "INFO":
            current_field = self.fields[self.current_field_index]

            if not user_input:
                response = f"I didn’t get that. {field_prompt(current_field)}"
                self._add_to_history("Bot", response)
                return response

            # Save field data
            self.candidate_data[current_field] = user_input
            response = self._move_to_next_field()
            self._add_to_history("Bot", response)
            return response

        # TECH_STACK STATE
        elif self.state == "TECH_STACK":
            self.tech_list = [t.strip() for t in user_input.split(",") if t.strip()]
            if not self.tech_list:
                response = "Please list at least one technology in your stack."
                self._add_to_history("Bot", response)
                return response

            self.state = "QUESTIONS"

            responses = []
            for tech in self.tech_list:
                prompt = f"List exactly 3 to 5 challenging interview questions for {tech}. Only output the questions, no explanations."
                answer = self.model_handler.generate_response(prompt).strip()

                # Remove accidental prompt echo
                if answer.lower().startswith(prompt.lower()):
                    answer = answer[len(prompt):].strip()

                # Fallback if model returns empty
                if not answer:
                    answer = "(No questions generated — please try again.)"

                responses.append(f"\n{tech}\n\n{answer}")

            final_response = "\n\n".join(responses)
            self._add_to_history("Bot", final_response)
            return final_response

        # QUESTIONS STATE
        elif self.state == "QUESTIONS":
            save_candidate_data(self.candidate_data)
            self.state = "END"
            response = farewell_prompt()
            self._add_to_history("Bot", response)
            return response

        # END or Fallback
        return fallback_response()
