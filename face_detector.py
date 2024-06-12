import cv2
import numpy as np
import requests
import os

# Verify that the files exist
if not os.path.exists('deploy.prototxt'):
    print("The deploy.prototxt file is not found in the current directory.")
if not os.path.exists('res10_300x300_ssd_iter_140000.caffemodel'):
    print("The res10_300x300_ssd_iter_140000.caffemodel file is not found in the current directory.")

# Charge the model
try:
    net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'res10_300x300_ssd_iter_140000.caffemodel')
    print("Model loaded successfully.")
except cv2.error as e:
    print(f"Error loading the model: {e}")
    net = None

# Function to download the image from a URL
def download_image(url):
    response = requests.get(url)
    image_data = np.frombuffer(response.content, np.uint8)
    image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
    return image

# URL of the image in Google Drive
image_url = 'https://drive.google.com/uc?export=download&id=1mL9_9heN9n2shCjL74oeb2NZohf0qXHR'

# Download the image
image = download_image(image_url)

if image is None:
    print(f"Unable to download image from URL: {image_url}")
elif net is not None:
    # Preprocess the image
    h, w = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
                                 (300, 300), (104.0, 177.0, 123.0))

    net.setInput(blob)
    detections = net.forward()

    # Drawing rectangles around the detected faces
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # threshold of confidence
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x, y, x1, y1) = box.astype("int")
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 2)

    # Display the image with the detected faces
    cv2.imshow('Detected Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
