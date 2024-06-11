from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from openai import OpenAI

class RequestModel(BaseModel):
    system_content: str
    user_content: str

app = FastAPI()

# Read the API key from the file
with open('secret_api_key.txt', 'r') as file:
    api_key = file.read().strip()

client = OpenAI(
   api_key=api_key
 )


@app.post("/process_text/")
async def process_text(request: RequestModel):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": request.system_content},
            {"role": "user", "content": request.user_content}
        ]
    )
    message_content = completion.choices[0].message.content
    return {"response": message_content}

if __name__ == "__main__":
    uvicorn.run(app, host="194.59.40.99", port=7990)