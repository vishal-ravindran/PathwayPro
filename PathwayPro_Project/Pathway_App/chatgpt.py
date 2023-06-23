import openai
import json
import re
from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv('API_KEY')




model = 'text-davinci-003'
temp = 0
tokens = 256
n_val = 1


def generate_response(prompt):
    response = openai.Completion.create(
        engine=model,  # which model to use
        prompt=prompt,
        max_tokens=tokens,  # Tokens are chunks of text, which can be as short as one character or as long as one word. By setting max_tokens, you can control the length of the response.
        temperature=temp,  # controls the randomness of the generated response. A higher value like 1.0 makes the output more diverse and creative, while a lower value like 0.2 makes it more focused and deterministic.
        n=n_val,  # represents the number of completions to generate for a single prompt.
        stop=None,  # If a stop string is provided, the model will stop generating text when it encounters that string in the output.
        echo=False  # Setting echo=True instructs the API to include the original prompt in the response, making it easier to see the context of the conversation.
    )
    return response.choices[0].text.strip()

# def main():
#     prompt = ""
#     user_input = input("Please enter your current job title...")
#     prompt += "\nFind NOC code for the following job title " + user_input.strip()

#     response = generate_response(prompt)
#     prompt += "\nAI: " + response.strip()
#     print(prompt)
#     print(response.strip())

#     numbers = re.findall(r'\d+', response)

#     noc_code = f"""
#     I am doing research on skills and tools commonly required by various occupations. My primary reference is the National Occupation Classification (NOC) developed by the Government of Canada. Based on NOC code, provide me with a list of the top skills and tools used on the job. Please provide a response in JSON format only, for the NOC code {numbers[0]}. Include nodes for "title", "skills", and "tools".
#     """

#     response = generate_response(noc_code)
#     prompt += "\nAI: " + response.strip()
#     print(prompt)
#     print(response.strip())

# if __name__ == "__main__":
#     main()
