import cv2
import numpy as np
import time
from PIL import ImageGrab
from win32api import GetSystemMetrics

# Define the recording duration in seconds
recording_duration = 13  # Adjust as needed

# Get screen dimensions
screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (screen_width, screen_height))

# Start recording
start_time = time.time()
while (time.time() - start_time) < recording_duration:
    # Capture the screen
    screen = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))  # Capture the whole screen
    frame = np.array(screen)  # Convert the screen capture to a numpy array
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert to BGR format for OpenCV
    out.write(frame)

# Release resources
out.release()
print("Recording finished!")
