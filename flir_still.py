import cv2

def capture_frame(rtsp_url, save_path="captured_frame1.jpg"):
    cap = cv2.VideoCapture(rtsp_url)
    
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(save_path, frame)
        print(f"Frame saved to {save_path}")
    else:
        print("Failed to capture frame.")
    
    cap.release()

# Usage
# For H264 encoding and the feed seen in the web interface:
rtsp_url = "rtsp://admin:qzIRge@169.254.218.190/avc/"
capture_frame(rtsp_url)
