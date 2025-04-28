from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
import logging 
from datetime import datetime
import shutil
import os
import whisper


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = whisper.load_model("base")
def whisper_stt(audio_file):
    """
    Pass audio file to get text output
    """
    logging.info("getting trascription")
    result = model.transcribe(audio_file, task="transcribe", language="en")
    return result['text']

@app.post("/stt")
async def speech_to_text(audio_file: UploadFile = File(...)):
    
    temp_file_path = f"temp_{audio_file.filename}"
    logging.info(f"{str(datetime.now())} Received audio: {audio_file.filename}") 
    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(audio_file.file, buffer)

        transcription = whisper_stt(temp_file_path)
        logging.info(f"transcribed text {transcription}")
        os.remove(temp_file_path)

        logging.info(f"{str(datetime.now())} Transcribed audio: {transcription}")
        return {"transcription": transcription}

    except Exception as e:
        os.remove(temp_file_path)
        logging.error(f"{str(datetime.now())} Error in speech-to-text: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def health_check():
    return {"status": "Authentication service is running"}
