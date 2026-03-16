# Used Gemini 3: https://gemini.google.com/share/b9a2f0aae7b2

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from transformers import pipeline
import tempfile
import asyncio
import os

app = FastAPI()

print("Loading ASR models into memory... This might take a minute.")
# We load the models using your exact Hugging Face repository IDs
sindhi_pipe = pipeline("automatic-speech-recognition", model="dvm14/whisper-small-sindhi")

akan_pipe = pipeline("automatic-speech-recognition", model="tiffany101/whisper-twi-v2") 
print("Models loaded successfully!")

@app.post("/api/transcribe/{language}")
async def transcribe(language: str, file: UploadFile = File(...)):
    if language not in ["sindhi", "akan"]:
        raise HTTPException(status_code=400, detail="Language not supported.")
    
    try:
        audio_bytes = await file.read()
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name
            
        pipe = sindhi_pipe if language == "sindhi" else akan_pipe
        
        # THE FIX: Run the heavy inference in a background thread
        # This prevents the web server from freezing!
        result = await asyncio.to_thread(pipe, tmp_path)
        
        os.remove(tmp_path)
        
        return {"transcription": result["text"]}
            
    except Exception as e:
        print(f"CRITICAL ERROR: {repr(e)}")
        return JSONResponse(status_code=500, content={"error": str(e)})

# Mount the frontend directory
app.mount("/", StaticFiles(directory="static", html=True), name="static")