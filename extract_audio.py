import os.path
import subprocess
from pathlib import Path

def extract_audio(input_file, output_directory="audios"):
    input_path = Path(input_file)
    output_directory_path = Path(output_directory)
    output_file = output_directory_path / input_path.with_suffix(".mp3").name
    ffmpeg_command = ["ffmpeg", "-i", input_file, "-vn", "-acodec", "libmp3lame", output_file]
    subprocess.run(ffmpeg_command)
    print(f"Extracted audio from {input_file} to {output_file}")