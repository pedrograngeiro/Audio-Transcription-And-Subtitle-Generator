import os.path
import subprocess

input_file = "videos/IELTS-Speaking-Test-Perfect-Band-9-IELTS-Advantage.mp4"
output_directory = "audios"
output_file = os.path.join(output_directory, os.path.basename(input_file).replace(".mp4", ".mp3"))

ffmpeg_command = f"ffmpeg -i {input_file} -vn -acodec libmp3lame {output_file}"
subprocess.run(ffmpeg_command, shell=True)

print(f"Extracted audio from {input_file} to {output_file}")