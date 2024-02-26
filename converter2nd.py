import os
from moviepy.editor import VideoFileClip
from tkinter.filedialog import askopenfilename

# Create a folder named "Audio Files" if it doesn't exist
audio_folder = "Audio Files"
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

# Open file dialog to select video file
video_file = askopenfilename()

# Create VideoFileClip object
video_clip = VideoFileClip(video_file)

# Extract audio from video clip
audio_clip = video_clip.audio

# Extract the file name and extension of the video file
video_file_name, video_file_ext = os.path.splitext(os.path.basename(video_file))

# Generate output audio file name based on input video file name
audio_file_name = os.path.join(audio_folder, video_file_name + ".mp3")

# Write audio to MP3 file with the same name as the video file
audio_clip.write_audiofile(audio_file_name)

print("Completed")  # Print message indicating completion
