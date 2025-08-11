# prompt_engineering.py

def greeting_prompt():
    return (
        "You are TalentScout, an AI Hiring Assistant. "
        "Greet the candidate, introduce yourself, and explain "
        "that you will collect basic information and ask technical questions "
        "based on their tech stack."
    )

# New: Step-by-step info prompts
def field_prompt(field_name):
    prompts = {
        "full_name": "Please tell me your full name.",
        "email": "Please provide your email address.",
        "phone": "Could you share your phone number?",
        "experience": "How many years of professional experience do you have?",
        "position": "What position(s) are you applying for?",
        "location": "Where are you currently located?"
    }
    return prompts[field_name]

def tech_stack_prompt():
    return (
        "List your tech stack including programming languages, "
        "frameworks, databases, and tools you are proficient in."
    )

# New: Generate questions per skill
def technical_questions_prompt(tech_list):
    prompt = "You are an AI interviewer. For each skill below, write 3–5 moderately challenging interview questions.\n"
    for tech in tech_list:
        prompt += f"\nSkill: {tech}\nQuestions:\n"
    prompt += "\nMake sure each question is relevant to the skill and tests real-world problem solving."
    return prompt


def farewell_prompt():
    return (
        "Thank you for your time! We’ll review your responses and contact you "
        "regarding the next steps in the hiring process."
    )
