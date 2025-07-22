🎬 SubIt – Subtitle Generator from Video
SubIt is a simple web app that allows users to upload a video and automatically generate accurate subtitles (.srt format) using audio transcription. Ideal for creators, educators, and editors who need quick and accurate subtitles without manual labor.


🚀 Features
🎥 Upload any video file (MP4, WebM, etc.)

🔊 Automatically extracts audio from the video

🧠 Uses speech recognition to transcribe spoken content

📄 Outputs downloadable .srt subtitle file

💻 Built with HTML, CSS, JavaScript, and Python (Flask)

📁 Folder Structure

SubIt/
│
├── static/
│   ├── style.css        # App styling
│   └── script.js        # Frontend logic (upload, fetch, player)
│
├── templates/
│   └── index.html       # Main HTML frontend
│
├── uploads/             # Temporary uploaded video storage
│
├── transcriber.py       # Audio extraction + transcription
├── srt_generator.py     # SRT file generation from transcript
├── app.py               # Flask backend server
├── requirements.txt     # Python dependencies
└── README.txt           # This file
🛠 Setup Instructions

1. Clone the Repository

git clone https://github.com/yourusername/SubIt.git
cd SubIt

2. Create and Activate a Virtual Environment (Recommended)

python -m venv venv
# Activate it:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Install FFmpeg

FFmpeg is required to extract audio from videos.

Windows: Download FFmpeg and add its bin folder to your system PATH

macOS: brew install ffmpeg

Linux: sudo apt install ffmpeg

To verify installation:

ffmpeg -version
▶️ Run the App

python app.py
Then open your browser and visit: http://127.0.0.1:5000

📤 How It Works
Upload a video via the frontend UI.

The Flask backend saves the video.

transcriber.py:

Extracts audio using FFmpeg

Transcribes speech to text using speech_recognition

srt_generator.py:

Converts transcript to .srt format

The .srt file is returned as a downloadable link.

📦 Dependencies
Flask

SpeechRecognition

srt

ffmpeg (external tool)

See requirements.txt for full list.

🧠 Future Improvements
Language selection for multilingual subtitle generation

Better timestamp chunking for accurate subtitle splits

UI enhancements and progress bar

Upload history and subtitle preview