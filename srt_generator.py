import srt
from datetime import timedelta
import uuid
import os

def generate_srt_file(segments):
    subtitles = []

    for i, seg in enumerate(segments):
        start = timedelta(seconds=seg["start"])
        end = timedelta(seconds=seg["end"])
        content = seg["text"].strip()
        subtitles.append(srt.Subtitle(index=i+1, start=start, end=end, content=content))

    srt_data = srt.compose(subtitles)
    srt_path = f"uploads/{uuid.uuid4()}.srt"

    with open(srt_path, "w", encoding="utf-8") as f:
        f.write(srt_data)

    return srt_path
