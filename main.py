import os
import whisper
from whisper.utils import get_writer
from extract_audio import extract_audio

def transcribe_audio(audio_file, model_name='small', output_directory='./srts/'):
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_file, fp16=False)

    srt_writer = get_writer("srt", output_directory)
    srt_writer(result, audio_file)

    audio_filename = os.path.basename(audio_file)
    txt_filename = os.path.splitext(audio_filename)[0] + ".txt"

    with open(os.path.join(output_directory, txt_filename), "w", encoding="utf-8") as txt:
        txt.write(result["text"])


# Usage
input_file = "video.mp4"
audio = extract_audio(input_file)
transcribe_audio(audio)