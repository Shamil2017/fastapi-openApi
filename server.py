from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/process_text/")
async def process_text(request: TextRequest):
    response_text = f"Received text: {request.text}"
    return {"response": response_text}

if __name__ == "__main__":
    uvicorn.run(app, host="194.59.40.99", port=7990)