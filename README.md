# Subtitle transcriber with AI

## Audio Extraction

The `extract_audio.py` script is used to extract audio from video files in MP4 format and save them as MP3 files   It uses `ffmpeg` to perform the extraction

### Usage

To use the script, you can call the `extract_audio` function by passing the path of the input file and, optionally, the output directory:

```python
from extract_audio import extract_audio

input_file = "videos/IELTS-Speaking-Test-Perfect-Band-9-IELTS-Advantage.mp4"
extract_audio(input_file)
```
By default, the extracted audio will be saved in the `audios` directory. You can specify a different output directory by passing it as the second argument to the `extract_audio` function.

### Audio Transcription
The `main.py` script is used to transcribe audio files into text and subtitle files using the Whisper model.

#### Usage

To use the script, you can call the `transcribe_audio` function by passing the path of the input audio file and, optionally, the output directory:

```python
from main import transcribe_audio

audio_file = "audios/IELTS-Speaking-Test-Perfect-Band-9-IELTS-Advantage.mp3"
transcribe_audio(audio_file)
```

By default, the transcribed text will be saved in the `texts` directory and the subtitle file will be saved in the `subtitles` directory. You can specify different output directories by passing them as the second and third arguments to the `transcribe_audio` function.
