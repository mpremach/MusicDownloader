from pydub import AudioSegment
import os

FFMPEG_PATH = os.path.join("ffmpeg", "bin", "ffmpeg.exe")
AudioSegment.converter = FFMPEG_PATH

