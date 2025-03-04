import os 
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

import base64

def encode_image(image_path):
    image_file = open(image_path,'rb')
    return base64.b64encode(image_file.read()).decode('utf-8')

encoded_image = encode_image("acne.jpg")

query = "Is there asomething wrong with my face?"
model = "llama-3.2-90b-vision-preview"

def analyze_image(query,model,encoded_image):
    client=Groq()
    messages = [
        {
            "role":"user",
            "content":[
                {
                    "type":"text",
                    "text":query
                },
                {
                    "type":"image_url",
                    "image_url": {
                        "url":f"data:image/jpeg;base64,{encoded_image}"
                    }
                }
            ]
        }
    ]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )
    
    return chat_completion.choices[0].message.content

res = analyze_image(query,model,encoded_image)
print(res)