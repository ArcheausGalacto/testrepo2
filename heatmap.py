import cv2
import numpy as np

def apply_heatmap_with_box(image_path, save_path="heatmap_boxed1.jpg", threshold_ratio=0.95):
    # Load the image in grayscale
    gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply the heatmap color map
    heatmap = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

    # Threshold the grayscale image to isolate the hottest parts
    _, thresholded = cv2.threshold(gray, threshold_ratio * 255, 255, cv2.THRESH_BINARY)
    
    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresholded.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Find the largest contour and draw its bounding box on the heatmap
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        cv2.rectangle(heatmap, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Draw the box in green color

    # Save the heatmap image with the box
    cv2.imwrite(save_path, heatmap)
    print(f"Heatmap with box saved to {save_path}")

# Usage
image_path = "C:\\Users\\Danie\\Desktop\\FLIR scripts\\captured_frame1.jpg"
apply_heatmap_with_box(image_path)
