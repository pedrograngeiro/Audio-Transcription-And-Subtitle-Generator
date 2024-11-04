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

### Dependencies
I used Python 3.9.11 and PyTorch to develop this project.\
You can install PyTorch using the following command:
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
See the official PyTorch website for more information:
https://pytorch.org/get-started/locally/

Openai-whisper is required to transcribe audio files. You can install it using the following command:

```bash
pip install -U openai-whisper
```

`ffmpeg` is required to extract audio from video files. You can download it from the official website:
https://ffmpeg.org/download.html
<br>
But you can also install it using the following command:
```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

You may need <a href='https://www.rust-lang.org/'>Rust</a> installed as well, in case <a href='https://github.com/openai/tiktoken'>tiktoken</a> does not provide a pre-built wheel for your platform. 
If you see installation errors during the command above, please follow the <a href='https://www.rust-lang.org/learn/get-started'>Getting started page</a> to install Rust development environment.
Additionally, you may need to configure the environment variable, e.g. . If the installation fails with , you need to install , e.g. by running:`pip installPATHexport PATH="$HOME/.cargo/bin:$PATH"No module named 'setuptools_rust'setuptools_rust`
```bash
pip install setuptools-rust
```

Read the official documentation for more information of whisper:
<a href='https://github.com/openai/whisper?tab=readme-ov-file'>Whisper</a>

### License
This project is licensed under the MIT License - see the LICENSE file for details.
