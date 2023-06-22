from flask import Flask, request, jsonify
import yt_dlp
import librosa
import os

app = Flask(__name__)

@app.route('/calculate_chord_sec', methods=['POST'])
def calculate_chord_sec():
    youtube_url = request.form.get('youtube_url')
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }]
    }
    script_path = os.path.abspath(__file__)
    folder_path = os.path.dirname(script_path)
    save_path = folder_path
    ydl_opts['outtmpl'] = f"{save_path}/testmusic.%(ext)s"
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    audio_file_path = os.path.join(folder_path, "testmusic.mp3")
    y, sr = librosa.load(audio_file_path)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    chord_sec = (60 / tempo) * 4
    duration = librosa.get_duration(y=y, sr=sr)
    tempo = round(tempo)
    youenter = duration/chord_sec
    return jsonify({'chord_sec': chord_sec, 'duration': duration , "tempo" : tempo})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)