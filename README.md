# Screen Recorder with Python 🎥🖥️

A Python-based screen recording application that captures your screen and saves it as a video file (`output.mp4`). Built using OpenCV, Pillow, and PyWin32 libraries.

---

## Features 🚀
- Records the entire screen in real-time.
- Saves the screen recording as an MP4 file.
- Adjustable recording duration.
- Lightweight and easy to use.

---

## Installation 📦

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/screen-recorder.git
   cd screen-recorder
   ```

2. **Install Dependencies**:
   ```bash
   pip install numpy opencv-python pillow pywin32
   ```

---

## How to Run 🏃‍♂️

1. **Run the Script**:
   ```bash
   python screen_recorder.py
   ```

2. **Output**:
   - The script records your screen for the specified duration.
   - The video is saved as `output.mp4` in the project directory.

---

## Customization ✏️

- **Recording Duration**:
  Adjust the `recording_duration` variable in the script:
  ```python
  recording_duration = 20  # Records for 20 seconds
  ```

- **Output File Name**:
  Change the file name in the `VideoWriter` initialization:
  ```python
  out = cv2.VideoWriter('my_recording.mp4', fourcc, 20.0, (screen_width, screen_height))
  ```

---

## Troubleshooting 🛠️

- Ensure all libraries are installed:
  ```bash
  pip install numpy opencv-python pillow pywin32
  ```

- If the video shows a black screen, ensure your system supports the `ImageGrab` functionality.

---

## License 📜

This project is licensed under the MIT License.

---

### Happy Recording! 😊
