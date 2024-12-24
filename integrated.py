import torch
import cv2
from ultralytics import YOLO
from pymavlink import mavutil
import time

model = YOLO(r"C:\Users\hp\Downloads\yolov8n_100e.pt")  

video_path = r"C:\Users\hp\Pictures\Camera Roll\WIN_20241224_11_15_58_Pro.mp4"

cap = cv2.VideoCapture(video_path)

# MAVLink connection setup
connection_string = "tcp:127.0.0.1:14550"  
master = mavutil.mavlink_connection(connection_string)
horizontal_fov=84.08436
vertical_fov=53.67973
# Wait for heartbeat
# print("Waiting for heartbeat...")
# master.wait_heartbeat()
# print("Heartbeat received. Autopilot connected.")

def set_gimbal_pitch_yaw(pitch_deg, yaw_deg):
    target_system = master.target_system
    target_component = master.target_component

    master.mav.command_long_send(
        target_system,                # target_system
        target_component,             # target_component
        mavutil.mavlink.MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW,  # Command
        0,                            # Confirmation (0: First transmission)
        pitch_deg,                    # Param 1: Pitch angle in degrees
        yaw_deg,                      # Param 2: Yaw angle in degrees
        float('nan'),                 # Param 3: Angular rate (not used)
        0,                            # Param 4: Gimbal flags (0 for default behavior)
        0,                            # Param 5: Reserved (set to 0)
        0,                            # Param 6: Reserved (set to 0)
        0                             # Param 7: Gimbal device ID (2 for primary gimbal)
    )
    print(f"Gimbal Command: Pitch={pitch_deg}°, Yaw={yaw_deg}°")

frame_center_x = 0
frame_center_y = 0

while cap.isOpened():
    success, frame = cap.read()

    if success:
        
        frame_height, frame_width, _ = frame.shape
        frame_center_x = frame_width // 2
        frame_center_y = frame_height // 2

        # YOLO inference
        results = model(frame)
        boxes = results[0].boxes.xywh.cpu().numpy()  
        if len(boxes) > 0:
           
            face_x, face_y, _, _ = boxes[0]

            
            x_deviation = face_x - frame_center_x
            y_deviation = face_y - frame_center_y

           
            scale_factor_yaw = horizontal_fov / frame_width
            scale_factor_pitch = vertical_fov / frame_height

            
            yaw_angle = -x_deviation * scale_factor_yaw  
            pitch_angle = -(y_deviation * scale_factor_pitch)  
            
            time.sleep(0.1)
            print(f'yaw angle :{yaw_angle}')
            print(f'pitch angle:{pitch_angle}')
            set_gimbal_pitch_yaw(pitch_angle, yaw_angle)

        
        annotated_frame = results[0].plot()
        cv2.imshow("YOLO Inference", annotated_frame)

        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
