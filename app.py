from flask import Flask, render_template, request, send_file
from transcriber import extract_audio_and_transcribe
from srt_generator import generate_srt_file
import os
import uuid

app = Flask(__name__, static_folder="static", template_folder="templates")
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def upload():
    file = request.files["video"]
    filename = f"{uuid.uuid4()}.mp4"
    video_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(video_path)

if __name__ == "__main__":
    app.run(debug=True)
