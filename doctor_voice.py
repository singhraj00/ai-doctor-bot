# setup text to speech  TTS Model (gTTS & ElevenLabs)


## setup text to speech  TTS Model (gTTs)
import os 
from gtts import gTTS

# def text_to_sppech_with_gTTs(input_text,output_filepath):
#     language='en'
#     audio_obj=gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audio_obj.save(output_filepath)

# text_to_sppech_with_gTTs(input_text='Hi Ai teams,build agents',output_filepath='gTTs_testing.mp3')

### setup text to speech  TTS Model (ElevenLabs)
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
import elevenlabs

load_dotenv()

ELEVENLABS_API_KEY = os.environ.get('ELVENLABS_API_KEY')




# def text_to_speech_with_eleven_labs(input_text,output_filepath):
#     client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio = client.generate(
#         text='Hi, How are you?',
#         voice='Aria',
#         output_format = 'mp3_22050_32',
#         model="eleven_turbo_v2"
#     )
#     elevenlabs.save(audio,output_filepath)

# text_to_speech_with_eleven_labs(input_text='Hi, how are you?',output_filepath='elevenlab_testing.mp3')

## setup2 Use model for text output to voice 

# use model for text to voice 

import subprocess
import platform

def text_to_sppech_with_gTTs(input_text,output_filepath):
    language='en'
    audio_obj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audio_obj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == 'Darwin':
            subprocess.run(['afplay',output_filepath])
        elif os_name=='Windows':
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])

        elif os_name=='Linux':
            subprocess.run(['aplay',output_filepath])
        else:
            raise OSError('Unsupported Operating Sytem')
    except Exception as e:
        print(f'An error occured while playing the audio: {e}')
        
# text_to_sppech_with_gTTs(input_text='Hi Ai teams,build agents',output_filepath='gTTs_testing_autoplay.mp3')

### setup text to speech  TTS Model (ElevenLabs)
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
import elevenlabs

load_dotenv()

ELEVENLABS_API_KEY = os.environ.get('ELVENLABS_API_KEY')




def text_to_speech_with_eleven_labs(input_text,output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text='Hi, How are you?',
        voice='Aria',
        output_format = 'mp3_22050_32',
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio,output_filepath)
    os_name = platform.system()
    try:
        if os_name == 'Darwin':
            subprocess.run(['afplay',output_filepath])
        elif os_name=='Windows':
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])

        elif os_name=='Linux':
            subprocess.run(['aplay',output_filepath])
        else:
            raise OSError('Unsupported Operating Sytem')
    except Exception as e:
        print(f'An error occured while playing the audio: {e}')
        

# text_to_speech_with_eleven_labs(input_text='Hi, how are you?',output_filepath='elevenlab_testing_autoplay.mp3')