import whisper
import openai
import librosa
import os 
from pathlib import Path
import soundfile as sf
import io
from app.const import USER_input, ASSISTANT_output, PROMPT
import dotenv

dotenv.load_dotenv()

import time

MIN_Length = 30
MAX_Length = 200
TRANSCRIPT_MODEL = "base"
GPT_MODEL = 'gpt-3.5-turbo'
MyText = ""
summarize_text = ""
TIME_TO_RECO = 0
TIME_TO_SUMM = 0
audio = None
API_KEY = os.getenv("API_KEY")

# Note: You need to set the API_KEY in the .env file
# Also these are the default values for the Azure API
# You can change them to your own values

openai.api_type = "azure"
openai.api_base = "your-azure-api-base-here"
openai.api_version = "2023-07-01-preview"
openai.api_key = API_KEY


def call_api(text):
    response = openai.ChatCompletion.create(
        engine="Arken-AI-gpt35",
        messages = [{"role":"system","content":"Your name is Arken,you are an AI assistant that write a clinical letter with a clear action plan at the end, based on the conversation."},
                        {"role":"user", "content":USER_input},
                        {"role":"assistant", "content":ASSISTANT_output},
                        {'role': 'user', 'content': text}],
        temperature=0.7,
        max_tokens=2000,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    return response.choices[0].message.content


def get_response(audio_file):
    PROMPT = "write a doctor's letter with a clear action plan at the end, based on the following conversation:"
    t1 = time.time()
    audio, _ = librosa.load(audio_file , sr=16000)
    model = whisper.load_model(TRANSCRIPT_MODEL)

    MyText = model.transcribe(audio, fp16=False)
    MyText = MyText["text"]
    t2 = time.time()
    transc_time = t2 - t1

    Final_Text = PROMPT + '\n' + MyText
    t1 = time.time()
    gpt_response = call_api(Final_Text)
    t2 = time.time()
    gpt_time = t2 - t1

    return {'transcription':MyText, 'response':gpt_response}








