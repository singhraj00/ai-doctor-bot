import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s %(message)s')


def record_audio(file_path,timeout=20,phrase_time_limit=None):
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            logging.info('start speaking now..')

            ## record audio
            audio_data = recognizer.listen(source,timeout=timeout,phrase_time_limit=phrase_time_limit)
            logging.info("recording completed..")

            ## convert recorded audio to mp3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path,format="mp3",bitrate="128k")

            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f'An error occured {e}')


audio_file_path = 'patience_voice_test.mp3'

#record_audio(audio_file_path)


## setup speech to text for transcription

from groq import Groq
import os 
from dotenv import load_dotenv

load_dotenv()


GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
stt_model = "whisper-large-v3"


def transcribe_with_groq(stt_model,audio_file_path,GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)

    audio_file = open(audio_file_path,'rb')

    transcription = client.audio.transcriptions.create(
    model=stt_model,
    file=audio_file,
    language='en'
    )

    return transcription.text