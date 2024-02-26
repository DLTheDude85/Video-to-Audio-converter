#!/bin/bash

# Run ytdownloader.py to download the YouTube video and output its file path
VIDEO_FILE=$(python ytdownloader.py)

# Check if the video file exists
if [ -f "$VIDEO_FILE" ]; then
    # Specify the output folder
    OUTPUT_FOLDER="Youtube Audio"

    # Create the output folder if it doesn't exist
    if [ ! -d "$OUTPUT_FOLDER" ]; then
        mkdir "$OUTPUT_FOLDER"
    fi

    # Run converter.py with the video file as input and the output folder
    python converter.py "$VIDEO_FILE" "$OUTPUT_FOLDER"
else
    echo "Failed to download the video."
fi
