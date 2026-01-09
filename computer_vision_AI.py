# Computer Vision Libaries and Operations
"""1. OpenCV (Open Source Computer Vision Library): A widely used library for computer vision tasks, including image and video processing, object detection, and facial recognition."""
#First, do "pip install opencv-python matplotlib"
import cv2 #for image processing
from matplotlib import pyplot as plt 
# import matplotlib.pyplot as plt

"""2. Load an image using cv2 path"""
image_path = 'tablesetting_prod.png'  # Replace with your image path
image = cv2.imread(image_path)

"""3. Convert BGR to RGB or Grayscale for displaying correctly with matplotlib"""
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

"""4. Apply Gausian blur to image"""
blurred_image = cv2.GaussianBlur(image_gray, (5, 5), 0)

"""5. Detect edges using Canny Edge Detection Algorithm"""
edges = cv2.Canny(blurred_image, 50, 150)

"""6. Display original and processed images using matplotlib"""
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Edge Detected Image')
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.show()