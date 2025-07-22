import whisper
import ffmpeg
import os

model = whisper.load_model("base")  # Use "small" or "medium" if you want better accuracy

def extract_audio_and_transcribe(video_path):
    audio_path = video_path.replace(".mp4", ".mp3")

    ffmpeg.input(video_path).output(audio_path).run(overwrite_output=True)

    result = model.transcribe(audio_path)
    return result["segments"]
