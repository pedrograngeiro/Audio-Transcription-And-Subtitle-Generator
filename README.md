# Subtitle transcriber with AI

## Audio Extraction

The `extract_audio.py` script is used to extract audio from video files in MP4 format and save them as MP3 files   It uses `ffmpeg` to perform the extraction

### Uso

To use the script, you can call the `extract_audio` function by passing the path of the input file and, optionally, the output directory:

```python
from extract_audio import extract_audio

input_file = "videos/IELTS-Speaking-Test-Perfect-Band-9-IELTS-Advantage.mp4"
extract_audio(input_file)
```
By default, the extracted audio will be saved in the audios directory. You can specify a different output directory by passing it as the second argument to the extract_audio function.
