import cv2
import numpy as np


# OpenCV Python Quiz

# Welcome to the OpenCV quiz! Follow the instructions below:
#
# 1. Complete the functions in `main.py`.
# 2. Each function corresponds to a quiz question,
#    follow instruction in comment above the function
# 3. Each function accepts a cv2 image and returns a cv2 image as well
# 4. You must use the parameters provided to the function
# 5. Do not rename the functions or change the parameters.
# 6. Push your code to your GitHub repository.

# The kernel is a tuple of two integers (x,y) eg. (5,5)
# Use it as is in the function parameters without changes

# 1. Blur an Image using GaussianBlur (2 point)
def blur_image(img, kernel, sigmaX):
    blurred_img = cv2.GaussianBlur(img, kernel, sigmaX)
    return blurred_img


# 2. Apply Canny, then Dilate, then Erode (3 points)
def canny_dilate_erode(img, low_threshold, high_threshold, kernel, iterations):
    edges = cv2.Canny(img, low_threshold, high_threshold)
    
    dilated = cv2.dilate(edges, kernel, iterations=iterations)
    
    eroded = cv2.erode(dilated, kernel, iterations=iterations)
    
    return eroded


# 3. Convert to Grayscale (2 point)
def convert_to_grayscale(img):
    # Read the image normally **then** convert it to grayscale
    # Important: Do not read the image as grayscale
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return grayscale_img


# 4. Draw Rectangle (1 point)
def draw_rectangle(img, start_point, end_point, color, thickness):
    img_with_rectangle = cv2.rectangle(img, start_point, end_point, color, thickness)
    return img_with_rectangle


# 5. Resize Image (2 points)
def resize_image(img, scale_percent):
    # Scale percent is integer value eg. 20,50,70 is valid
    # Important: Use INTER_AREA interpolation
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    
    resized_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    
    return resized_img

