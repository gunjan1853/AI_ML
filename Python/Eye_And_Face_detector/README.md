# Eye Detector Project

## Project Name
Real-time Eye Detection using OpenCV

## Objective
Build a simple computer vision project that detects faces and eyes in real-time from webcam feed using Haar Cascade classifiers.

## Requirements
- Python 3.x
- OpenCV (opencv-python)

## Installation
```bash
pip install -r requirements.txt
```

## How to Run
```bash
python main.py
```
Press **Q** to exit the application.

## Output
The program opens a window showing webcam feed with:
- Blue rectangles around detected faces
- Green rectangles around detected eyes
- FPS counter
- Face count
- Eye count

## Future Improvements
- Add smile detection
- Save detected faces to disk
- Use DNN-based face detector for better accuracy
- Add glasses detection
- Create a GUI with tkinter