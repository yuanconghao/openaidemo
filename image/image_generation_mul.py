import os
import openai
import time

# Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

# generate nums images
nums = 2
url_list = []
for i in range(nums):
    response = openai.Image.create(
        prompt="ai programmer using the Picasso style",
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    url_list.append(image_url)
    time.sleep(10)

print(url_list)
