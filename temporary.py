import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the text you want to translate
input_text = "Hello, how are you?"

response = openai.Completion.create(
    engine="text-davinci-003",  # Use the desired GPT-3 engine
    prompt="Translate the following English text to French: '{}'".format(input_text),
    max_tokens=50  # Adjust as needed
)

translated_text = response.choices[0].text.strip()

print("Translated Text:", translated_text)
