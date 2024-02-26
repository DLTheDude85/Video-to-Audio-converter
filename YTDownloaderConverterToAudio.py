import os
from moviepy.editor import VideoFileClip
from tkinter.filedialog import askopenfilename
from pytube import YouTube
from mutagen.mp3 import MP3, EasyMP3

def extract_audio(video_file, output_folder):
    video_clip = VideoFileClip(video_file)
    audio_clip = video_clip.audio

    # Extract the file name and extension of the video file
    video_file_name, _ = os.path.splitext(os.path.basename(video_file))

    # Generate output audio file name based on input video file name
    audio_file_name = os.path.join(output_folder, video_file_name + ".mp3")

    # Write audio to MP3 file with the same name as the video file
    audio_clip.write_audiofile(audio_file_name)

    return audio_file_name

def write_metadata(audio_file, artist, album):
    audio = EasyMP3(audio_file)

    # Set artist and album information as metadata tags
    audio["artist"] = artist
    audio["album"] = album

    # Save the metadata changes to the audio file
    audio.save()

if __name__ == "__main__":
    # Create a folder named "Youtube videos" if it doesn't exist
    videos_folder = "Youtube videos"
    if not os.path.exists(videos_folder):
        os.makedirs(videos_folder)

    try:
        # Ask the user to input the YouTube URL
        url = input("Enter the YouTube URL: ")

        yt = YouTube(url)

        # Get the highest resolution stream
        yd = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        # Download the video to the "Youtube videos" folder
        video_file = yd.download(videos_folder)

        # Extract audio and get the audio file path
        audio_file = extract_audio(video_file, "Audio Files")

        # Get artist and album information
        artist = input("Enter artist name: ")
        album = input("Enter album name: ")

        # Write metadata to the audio file properties
        write_metadata(audio_file, artist, album)
        
        print(f"Title: {yt.title} By Artist: {artist} Album: {album} has been added to the library.")
        
    except Exception as e:
        print("An error occurred:", str(e))
