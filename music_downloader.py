#Standard library imports
import os # For file path manipulations

#Third party imports
from pydub import AudioSegment # Converting audio formats to mp3
from yt_dlp import YoutubeDL # For downloading audio from YouTube and other platforms
from mutagen.easyid3 import EasyID3 # For editing mp3 metadata


FFMPEG_PATH = os.path.join("ffmpeg", "bin", "ffmpeg.exe") # Path to ffmpeg executable
AudioSegment.converter = FFMPEG_PATH # Set ffmpeg path for pydub
MUSIC_FOLDER = os.path.join(os.path.expanduser("~"), "Music") # Default music folder
DOWNLOAD_FOLDER = os.path.join(MUSIC_FOLDER, "MusicDownloader") # Folder to save downloaded music
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True) # Create download folder if it doesn't exist
print(f"Download folder set to: {DOWNLOAD_FOLDER}")


def download_audio():

    # Ask the user to paste the URL of the track
    url = input("Paste YouTube or SoundCloud URL here: ").strip()

    ydl_opts = {
        'format': 'bestaudio/best', # Get best quality audio
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'), # Provide ydl with a template for name and file type and name
        'noplaylist': True, # Do not download playlists, only single videos even if in playlist
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url]) # Download the audio
        print("Download complete.")

download_audio()



