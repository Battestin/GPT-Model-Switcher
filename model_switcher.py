from openai import OpenAI
from dotenv import load_dotenv
import os
import tiktoken

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

model = "gpt-3.5-turbo"

encoding = tiktoken.encoding_for_model(model)

def load_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except IOError as e:
        print(f"Error loading file: {e}")

system_prompt = """
Identify the purchasing profile for each customer below.

The output format should be:

customer - describe the customer profile in 3 words
"""

user_prompt = load_file("Alura\GPT Python criando ferramentas com API\GPT - Model selector\data\purchase_list_100_customers.csv")

tokens_list = encoding.encode(system_prompt + user_prompt)
number_of_tokens = len(tokens_list)
print(f"Number of iput tokens: {number_of_tokens}")
output_tokens_expected = 2048

if number_of_tokens >= 4096 - output_tokens_expected:
    model = "gpt-4"

print(f"Using model: {model}")

messages_list = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

response = client.chat.completions.create(
    model=model,
    messages=messages_list
)

print(response.choices[0].message.content)