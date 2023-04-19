import openai
import requests as req
from PIL import Image
from io import BytesIO

response = openai.Image.create_edit(
    image=open("./data/image.png", "rb"),
    mask=open("./data/mask.png", "rb"),
    prompt="空白地方画两只手扶着拐杖",
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']
response = req.get(image_url)
image = Image.open(BytesIO(response.content))
image.show()
print(image_url)
