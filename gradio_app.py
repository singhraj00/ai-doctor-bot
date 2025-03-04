## Create Voice Bot UI
from doctor import encode_image,analyze_image
from patience_voice import record_audio,transcribe_with_groq
from doctor_voice import text_to_sppech_with_gTTs,text_to_speech_with_eleven_labs
import gradio as gr
import os


system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose.
            What's in this image?. Do you find anything wrong with it medically?
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot,
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""

def process_input(audio_filepath,image_filepath):
    speech_to_text_output=transcribe_with_groq(GROQ_API_KEY=os.environ.get('GROQ_API_KEY'),audio_file_path=audio_filepath,stt_model='whisper-large-v3')
    if image_filepath:
        doctor_response = analyze_image(query= system_prompt + speech_to_text_output,encoded_image=encode_image(image_filepath),model='llama-3.2-11b-vision-preview')
    else:
        doctor_response="No image provided for me to analyze"

    voice_of_doctor = text_to_sppech_with_gTTs(doctor_response,'final.mp3')
    return speech_to_text_output,doctor_response,voice_of_doctor


iface = gr.Interface(
    fn=process_input,
    inputs=[
        gr.Audio(sources=['microphone'],type='filepath'),
        gr.Image(type='filepath')
    ],
    outputs = [
        gr.Textbox(label='Speech to text'),
        gr.Textbox(label='Doctor response'),
        gr.Audio('Temp.mp3')
    ],
    title='AI Doctor with Vision and Voice',
)

iface.launch(debug=True)