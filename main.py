# Used Gemini 3: https://gemini.google.com/share/b9a2f0aae7b2

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from transformers import pipeline
import tempfile
import os

app = FastAPI()

print("Loading ASR models into memory... This might take a minute.")
# We load the models using your exact Hugging Face repository IDs
sindhi_pipe = pipeline("automatic-speech-recognition", model="dvm14/whisper-small-sindhi")

# Double-check that this is your correct Akan model ID!
akan_pipe = pipeline("automatic-speech-recognition", model="dvm14/whisper-small-akan") 
print("Models loaded successfully!")

@app.post("/api/transcribe/{language}")
async def transcribe(language: str, file: UploadFile = File(...)):
    if language not in ["sindhi", "akan"]:
        raise HTTPException(status_code=400, detail="Language not supported.")
    
    try:
        audio_bytes = await file.read()
        
        # Save the audio to a temporary file so transformers can process it cleanly
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name
            
        # Select the correct pipeline
        pipe = sindhi_pipe if language == "sindhi" else akan_pipe
        
        # Run the actual inference locally!
        result = pipe(tmp_path)
        
        # Clean up the temporary file
        os.remove(tmp_path)
        
        return {"transcription": result["text"]}
            
    except Exception as e:
        print(f"CRITICAL ERROR: {repr(e)}")
        return JSONResponse(status_code=500, content={"error": str(e)})

# Mount the frontend directory
app.mount("/", StaticFiles(directory="static", html=True), name="static")