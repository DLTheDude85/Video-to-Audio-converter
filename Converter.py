import sys
import os
from moviepy.editor import VideoFileClip

def extract_audio(video_file):
    video_clip = VideoFileClip(video_file)
    audio_clip = video_clip.audio

    # Extract the file name and extension of the video file
    video_file_name, _ = os.path.splitext(os.path.basename(video_file))

    # Generate output audio file name based on input video file name
    audio_file_name = video_file_name + ".mp3"

    audio_clip.write_audiofile(audio_file_name)

    print("Completed")  # Print message indicating completion

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python converter.py <video_file>")
        sys.exit(1)

    video_file = sys.argv[1]
    extract_audio(video_file)
