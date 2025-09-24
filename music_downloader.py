#Standard library imports
import os # For file path manipulations

#Third party imports
from pydub import AudioSegment #Converting audio formats to mp3
from yt_dlp import YoutubeDL # For downloading audio from YouTube and other platforms
from mutagen.easyid3 import EasyID3 # For editing mp3 metadata


FFMPEG_PATH = os.path.join("ffmpeg", "bin", "ffmpeg.exe") # Path to ffmpeg executable
AudioSegment.converter = FFMPEG_PATH # Set ffmpeg path for pydub
MUSIC_FOLDER = os.path.join(os.path.expanduser("~"), "Music") # Default music folder
DOWNLOAD_FOLDER = os.path.join(MUSIC_FOLDER, "MusicDownloader") # Folder to save downloaded music
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True) # Create download folder if it doesn't exist
print(f"Download folder set to: {DOWNLOAD_FOLDER}")

