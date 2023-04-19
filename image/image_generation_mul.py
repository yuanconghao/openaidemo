import os
import openai
import time

# Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

# generate nums images
prompts = [
    "the Imperial Palace using Michelangelo Style",
    "the Imperial Palace using Leonardo da Vinci Style",
    "the Imperial Palace using Francisco Goya Style",
    "the Imperial Palace using Claude Monet Style",
    "the Imperial Palace using Pablo Picasso Style",
    "the Imperial Palace using Jackson Pollock Style",
    "the Imperial Palace using Wassily Kandinsky Style",
]

nums = 2
url_list = []

for prompt in prompts:
    for i in range(nums):
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        print(image_url)
        url_list.append(image_url)
        time.sleep(5)

print(url_list)
