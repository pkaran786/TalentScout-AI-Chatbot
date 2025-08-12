# 🤖 TalentScout AI Hiring Assistant

## Project Overview
TalentScout AI is an intelligent hiring assistant chatbot designed for **initial screening of technology candidates**.  
It collects essential candidate details, asks about their **tech stack**, and generates **technical interview questions** tailored to the technologies provided.  

The chatbot is built using **Python**, **Streamlit** for UI, and a **Large Language Model (LLaMA-2)** for dynamic question generation.  
Candidate data is stored locally in JSON format for simulated backend processing.  

---

## Features
✅ Greet and introduce the chatbot’s purpose  
✅ Collect candidate details (name, email, phone, experience, position, location)  
✅ Ask for tech stack (programming languages, frameworks, tools)  
✅ Generate **3–5 tech-specific interview questions** per skill  
✅ Maintain conversation context and flow  
✅ Exit gracefully on keywords like `bye`, `quit`, `exit`  
✅ Save candidate data in `candidates.json`  

---

## Installation Instructions
1. **Clone this repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/talentscout-ai-chatbot.git
   cd talentscout-ai-chatbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Mac/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit transformers torch accelerate sentencepiece pandas
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

---

## Usage Guide
1. Open the **Streamlit UI** (automatically opens in browser after running `streamlit run app.py`).  
2. The chatbot will:
   - Greet you and explain its purpose.
   - Collect your basic details.
   - Ask for your tech stack.
   - Generate tailored interview questions.
3. You can end the conversation anytime with commands like `bye`, `exit`, `quit`.

---

## Technical Details
- **Language:** Python 3.x  
- **Frontend:** Streamlit  
- **Model:** `meta-llama/Llama-2-7b-chat-hf` (loaded via Hugging Face Transformers)  
- **Libraries:**  
  - `streamlit` – UI  
  - `transformers` – Model handling  
  - `torch` – Backend for LLM  
- **Data Storage:** Local JSON file (`data/candidates.json`)  

**Folder Structure**
```
.
├── app.py                 # Streamlit interface
├── chatbot.py              # Conversation logic
├── model_handler.py        # LLM model loading & response generation
├── prompt_engineering.py   # Predefined prompts
├── data_handler.py         # Save/load candidate data
├── utils.py                # Helper functions
└── data/
    └── candidates.json     # Saved candidate records
```

---

## Prompt Design
Prompts are defined in `prompt_engineering.py` and are designed for:  
- **Greeting Prompt:** Introduce TalentScout AI and explain the process.  
- **Field Prompts:** Request candidate details step-by-step (name, email, etc.).  
- **Tech Stack Prompt:** Ask for programming languages, frameworks, databases, tools.  
- **Question Generation Prompt:** Generate 3–5 interview questions per skill.  
- **Farewell Prompt:** Conclude the conversation politely.  

---

## Challenges & Solutions
### **Challenge 1:**  
Loading LLaMA-2 on limited hardware caused memory errors.  
**Solution:**  
Used `load_in_4bit=True` and `device_map="auto"` to fit model in GPU RAM.

### **Challenge 2:**  
Ensuring conversation context for smooth flow.  
**Solution:**  
Maintained an internal `conversation_history` string and chatbot state machine.

### **Challenge 3:**  
Handling empty or unexpected inputs.  
**Solution:**  
Added fallback responses and re-ask prompts if user input is missing.

---

## Future Enhancements
- Fallback to predefined question bank (`sample_questions.json`) if model fails  
- Deployment to cloud (AWS/GCP) for public access  
- Sentiment analysis during interview  
- Multilingual support  

