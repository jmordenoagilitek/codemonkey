import openai
from dotenv import load_dotenv
import os

TXT_PATH = "Partnerships User Story.txt"
ENV_PATH = 'key.env'
AI_INSTRUCTIONS = "Process the following user stories, then output a logical feature set that is correctly grouped. Identify avatars:"
AI_ROLE = "You are a product manager working for a software company."
MAX_TOKENS = 4000

class OpenAITextProcessor:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def read_text_from_file(self, txt_path):
        with open(txt_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
        return text_content

    def generate_instructions(self):
        instructions = AI_INSTRUCTIONS
        return instructions

    def send_text_to_openai(self, text_content, instructions="", max_tokens=MAX_TOKENS):
        full_content = f"{instructions}\n\n{text_content}" if instructions else text_content
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": AI_ROLE},
                {"role": "user", "content": full_content}
            ],
            max_tokens=max_tokens
        )
        return response['choices'][0]['message']['content']

def main():
    load_dotenv(dotenv_path=ENV_PATH)

    openai_api_key = os.getenv("OPENAI_API_KEY")

    processor = OpenAITextProcessor(api_key=openai_api_key)

    txt_path = TXT_PATH

    text_content = processor.read_text_from_file(txt_path)
    print("Text read successfully")

    instructions = processor.generate_instructions()

    response = processor.send_text_to_openai(text_content, instructions=instructions)
    print("OpenAI response:", response)

if __name__ == "__main__":
    main()
