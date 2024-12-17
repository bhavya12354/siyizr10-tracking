
# Project: Advanced Scripts for Robotics and AI Applications

This repository is a collection of Python scripts designed for critical tasks in robotics and AI workflows. The scripts include functionality for checksum calculations, real-time object detection, and angle encoding for robotic systems.

## **Overview**

### 1. `crccalculator.py`
This module implements a CRC-16 (XMODEM) checksum calculator for validating hexadecimal command strings.
#### **Technical Details**
- CRC polynomial: `0x11021`
- Initial CRC: `0`
- XOR output: `0`
- Big-endian, non-reversed data input.
- Appends the calculated LSB and MSB to the command.

#### **Execution**
1. Input: Hexadecimal command string.
2. Processing: Converts the string into bytes, computes the CRC-16 checksum, and extracts the MSB and LSB.
3. Output: Appends the checksum to the command.

#### **Example**
```python
test_string = "55 66 01 01 00 00 00 0c 00"
crc_output = crc_calculator(test_string)
```
**Output**
```
CRC-16 (XMODEM): 0x1d0f
MSB: 1d
LSB: 0f
```

---

### 2. `detection.py`
Real-time object detection using a YOLOv8 model, suitable for AI-driven visual systems.

#### **Technical Specifications**
- Model: YOLOv8 (custom-trained weights).
- Framework: `torch` and `ultralytics`.
- Video Processing: Utilizes OpenCV for real-time frame capture and display.

#### **Workflow**
1. Load a custom YOLO model (`.pt` format).
2. Process a video frame-by-frame.
3. Perform inference and annotate detected objects.
4. Output: Displays annotated frames and logs bounding box coordinates.

#### **Execution**
- Replace the model path and video path as needed.
- Run the script, and press `q` to exit.

---

### 3. `set_angle.py`
Encodes yaw and pitch angles into two's complement hexadecimal format for robotic system commands.

#### **Technical Details**
- Input: Signed integer angles (yaw, pitch).
- Conversion:
  - Negative values: Two's complement representation.
  - Positive values: Standard hexadecimal conversion.
- Fixed bit-width: 16 bits.

#### **Execution**
1. Input yaw and pitch angles.
2. Outputs hexadecimal representations padded to 4 characters.

#### **Example**
Input:
```bash
provide the yaw angle: -45
provide the pitch angle: 30
```
**Output**
```
Pitch Hex: ffd2
Yaw Hex: 001e
```

---

## **Requirements**
Install dependencies using the following command:
```bash
pip install -r requirements.txt
```

## **Repository Structure**
| File               | Functionality                                              |
|--------------------|------------------------------------------------------------|
| `crccalculator.py` | Computes and appends CRC-16 checksum to hexadecimal commands.|
| `detection.py`     | Performs YOLO-based object detection on video input.        |
| `set_angle.py`     | Encodes yaw and pitch angles into hexadecimal format.       |

---

## **Getting Started**
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the desired script:
   ```bash
   python crccalculator.py
   python detection.py
   python set_angle.py
   ```

---

## **License**
This project is licensed under the MIT License.

## **Contributions**
Contributions are welcome. Open issues or submit pull requests for enhancements.

