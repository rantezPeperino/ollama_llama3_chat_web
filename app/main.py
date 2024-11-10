from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import ollama

app = FastAPI()

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

@app.post("/chat")
async def chat(request: PromptRequest):
    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {
                    "role": "user",
                    "content": request.prompt,
                },
            ],
        )
        return {"response": response["message"]["content"]}
    except Exception as e:
        return {"response": f"Error: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)