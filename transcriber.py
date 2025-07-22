import whisper
import ffmpeg
import os
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from hinglish_mapper import ITRANS_TO_HINGLISH

model = whisper.load_model("small")

def contains_devanagari(text):
    return any('\u0900' <= ch <= '\u097F' for ch in text)

def clean_hinglish(text):
    words = text.split()
    cleaned = []
    for word in words:
        cleaned.append(ITRANS_TO_HINGLISH.get(word, word)) 
    return " ".join(cleaned)

def extract_audio_and_transcribe(video_path):
    audio_path = video_path.replace(".mp4", ".mp3")
    ffmpeg.input(video_path).output(audio_path).run(overwrite_output=True)

    result = model.transcribe(audio_path)
    segments = result["segments"]

    final_transcript = []
    for seg in segments:
        original_text = seg["text"]
        if contains_devanagari(original_text):
            transliterated = transliterate(original_text, sanscript.DEVANAGARI, sanscript.ITRANS)
            hinglish = clean_hinglish(transliterated)
        else:
            hinglish = original_text

        final_transcript.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": hinglish
        })

    return final_transcript