import os
import openai

# Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

# generate nums images
response = openai.Image.create(
    prompt="ai programmer using the Picasso style",
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)
