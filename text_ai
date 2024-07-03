import openai
from dotenv import load_dotenv
import os

class OpenAITextProcessor:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def read_text_from_file(self, txt_path):
        with open(txt_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
        return text_content

    def generate_instructions(self):
        instructions = "Process the following user stories, then output a logical feature set that is correctly grouped. Identify avatars:"
        return instructions

    def send_text_to_openai(self, text_content, instructions="", max_tokens=4000):
        full_content = f"{instructions}\n\n{text_content}" if instructions else text_content
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a product manager woring for a software company."},
                {"role": "user", "content": full_content}
            ],
            max_tokens=max_tokens
        )
        return response['choices'][0]['message']['content']

def main():
    load_dotenv(dotenv_path='key.env')

    openai_api_key = os.getenv("OPENAI_API_KEY")

    processor = OpenAITextProcessor(api_key=openai_api_key)

    txt_path = "Partnerships User Story.txt"

    text_content = processor.read_text_from_file(txt_path)
    print("Text read successfully")

    instructions = processor.generate_instructions()

    response = processor.send_text_to_openai(text_content, instructions=instructions)
    print("OpenAI response:", response)

if __name__ == "__main__":
    main()
