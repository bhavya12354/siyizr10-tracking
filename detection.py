import torch
import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO(r"C:\Users\hp\Downloads\yolov8n_100e.pt")  # Load the YOLO model

# Open the video file
video_path = r"C:\Users\hp\Pictures\Camera Roll\WIN_20241213_22_26_00_Pro.mp4"
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLO inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLO Inference", annotated_frame)

        # Print the bounding box information
        print(results[0].boxes.xywh.cpu().numpy())  # Bounding box in [x, y, width, height] format

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
