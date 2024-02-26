from pytube import YouTube
import os

try:
    # Create a folder named "Youtube videos" if it doesn't exist
    videos_folder = "Youtube videos"
    if not os.path.exists(videos_folder):
        os.makedirs(videos_folder)
    
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")
    
    yt = YouTube(url)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()
    
    # Download the video to the "Youtube videos" folder
    yd.download(videos_folder)
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))
