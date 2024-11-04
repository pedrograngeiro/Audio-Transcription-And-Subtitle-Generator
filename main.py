import os

import whisper
from whisper.utils import get_writer

model = whisper.load_model('small')
audio = "audios/IELTS-Speaking-Test-Perfect-Band-9-IELTS-Advantage.mp3"
result = model.transcribe(audio, fp16=False)
output_directory = "./srts/"

srt_writer = get_writer("srt", output_directory)
srt_writer(result, audio)

audio_filename = os.path.basename(audio)
txt_filename = os.path.splitext(audio_filename)[0] + ".txt"

with open(os.path.join(output_directory, txt_filename), "w", encoding="utf-8") as txt:
    txt.write(result["text"])

