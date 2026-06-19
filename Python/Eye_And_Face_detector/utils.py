import cv2
import time


prev_time = 0


def calculate_fps():
    global prev_time
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
    prev_time = curr_time
    return int(fps)


def draw_text(frame, text, position, color=(255, 255, 255)):
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)