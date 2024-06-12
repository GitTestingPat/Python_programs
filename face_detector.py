import cv2
import numpy as np
import requests
import os

# Verify that the files exist
if not os.path.exists('deploy.prototxt'):
    print("El archivo deploy.prototxt no se encuentra en el directorio actual.")
if not os.path.exists('res10_300x300_ssd_iter_140000.caffemodel'):
    print("El archivo res10_300x300_ssd_iter_140000.caffemodel no se encuentra en el directorio actual.")

# Charge the model
try:
    net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'res10_300x300_ssd_iter_140000.caffemodel')
    print("Modelo cargado exitosamente.")
except cv2.error as e:
    print(f"Error al cargar el modelo: {e}")
    net = None

# Function to download the image from a URL
def download_image(url):
    response = requests.get(url)
    image_data = np.frombuffer(response.content, np.uint8)
    image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
    return image

# URL of the image in Google Drive
image_url = 'https://drive.google.com/uc?export=download&id=1mL9_9heN9n2shCjL74oeb2NZohf0qXHR'

# Descargar la imagen
image = download_image(image_url)

if image is None:
    print(f"No se pudo descargar la imagen desde la URL: {image_url}")
elif net is not None:
    # Preprocesar la imagen
    h, w = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
                                 (300, 300), (104.0, 177.0, 123.0))

    net.setInput(blob)
    detections = net.forward()

    # Dibujar rectángulos alrededor de los rostros detectados
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # umbral de confianza
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x, y, x1, y1) = box.astype("int")
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 2)

    # Mostrar la imagen con los rostros detectados
    cv2.imshow('Detected Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
