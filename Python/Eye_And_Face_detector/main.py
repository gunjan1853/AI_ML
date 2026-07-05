import cv2
from detector import EyeDetector
from utils import calculate_fps, draw_text


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    detector = EyeDetector()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame")
            break

        processed_frame, face_count, eye_count = detector.process_frame(frame)

        fps = calculate_fps()

        draw_text(processed_frame, f"FPS : {fps}", (10, 30))
        draw_text(processed_frame, f"Faces : {face_count}", (10, 60))
        draw_text(processed_frame, f"Eyes : {eye_count}", (10, 90))
        draw_text(processed_frame, "Press Q to Quit", (10, 120), (0, 0, 255))

        cv2.imshow("Eye Detector", processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()