import cv2
import numpy as np

def sobel_edge_detection(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (3, 3), 0)

    # Apply Sobel operator to detect edges
    sobelx = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3)

    # Calculate the gradient magnitude and direction
    gradient_magnitude = np.sqrt(sobelx**2 + sobely**2)
    gradient_direction = np.arctan2(sobely, sobelx)

    # Normalize the gradient magnitude to 0-255
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    return gradient_magnitude, gradient_direction

if __name__ == '__main__':
    # Load the image
    image = cv2.imread('image.jpg')  # Replace 'image.jpg' with your own image file

    # Apply Sobel edge detection
    edges, direction = sobel_edge_detection(image)

    # Display the original image and edges
    cv2.imshow('Original Image', image)
    cv2.imshow('Edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()