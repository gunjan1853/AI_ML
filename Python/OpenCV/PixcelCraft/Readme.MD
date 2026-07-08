# PixelCraft

A CLI-based image processing suite built with OpenCV and NumPy, supporting 15 chained image transformations — from basic brightness/contrast adjustments to Haar-cascade-based background blur and cartoon/pencil-sketch effects.

## Features

| # | Operation | Technique Used |
|---|-----------|-----------------|
| 1 | Brightness Enhancement | Linear transform (`α·x + β`) |
| 2 | Contrast Enhancement | Linear scaling around pixel intensity |
| 3 | Crop Image | Array slicing |
| 4 | Resize Image | Interpolation (`INTER_AREA`) |
| 5 | Rotate Image | Affine transformation matrix |
| 6 | Beauty Filter (Skin Smoothing) | Bilateral filtering |
| 7 | Sharpen Image | High-pass convolution kernel |
| 8 | Blur Image | Gaussian blur |
| 9 | Remove Noise | Non-Local Means denoising |
| 10 | Black & White | Grayscale conversion |
| 11 | Cartoon Effect | Adaptive threshold edges + bilateral filter |
| 12 | Pencil Sketch | Grayscale + inverted Gaussian blur (color dodge) |
| 13 | Edge Detection | Canny edge detector |
| 14 | Background Blur | Haar cascade face detection + selective blur |
| 15 | HDR Effect | Detail enhancement (edge-preserving filter) |
| 16 | Save Image | Export processed result |

## Requirements

```bash
pip install opencv-python numpy
```

## Usage

```bash
python photo_editor.py
```

1. Enter the path to your image when prompted (relative or absolute, no quotes).
2. Choose an operation from the menu — operations chain on top of each other in the same session.
3. Preview each result in a popup window; press any key to continue.
4. Select **Save Image** at any point to export the current state.
5. Select **Exit** to quit.

## Example

```
===== PixelCraft =====
Enter path to your image: ../Img/women.jpeg
✅ Loaded image: 1080x720 pixels

1. Brightness Enhancement
...
Enter your choice: 11   # Cartoon Effect
```

## Notes

- Background Blur requires a clear frontal face for detection; falls back to a center-crop blur if no face is found.
- Blur strength values must be odd numbers (the script auto-corrects even inputs).
- Designed as a learning project to explore OpenCV fundamentals: convolution, color space conversions, affine transforms, and classical (pre-deep-learning) computer vision techniques.

## Tech Stack

- Python
- OpenCV (`opencv-python`)
- NumPy

## Author

Built by Gunjan — B.Tech CSE, UIET Chandigarh (Panjab University)