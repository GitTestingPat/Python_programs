# Proyecto de Detección de Rostros con OpenCV y DNN

## Descripción

Este proyecto utiliza la biblioteca OpenCV junto con un modelo de Red Neuronal Profunda (DNN) preentrenado para detectar rostros en imágenes. La detección de rostros es una tarea fundamental en muchas aplicaciones, como la seguridad, la fotografía y las redes sociales. Este programa permite detectar rostros de manera precisa y eficiente.

## Funcionalidades

- **Detección precisa de rostros**: Utiliza un modelo DNN preentrenado para lograr una alta precisión en la detección de rostros.
- **Soporte para imágenes locales y en línea**: Puede procesar imágenes almacenadas localmente o descargar y procesar imágenes desde URLs.
- **Interfaz sencilla**: El código es fácil de entender y modificar, lo que permite su integración en otros proyectos.

## Ventajas y Beneficios

| Ventajas                      | Beneficios                                                   |
|-------------------------------|--------------------------------------------------------------|
| Alta precisión                | Detección confiable de rostros en diversas condiciones       |
| Utiliza modelos preentrenados | No se requiere entrenamiento adicional, listo para usar      |
| Soporte para múltiples fuentes| Procesa imágenes locales y en línea                          |
| Fácil de usar                 | Código claro y bien documentado para fácil integración       |

## Instalación

### Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes en tu sistema:

- **Python 3**: Si no tienes Python instalado, puedes descargarlo desde [python.org](https://www.python.org/downloads/).

### Instalación de Bibliotecas

Instala las bibliotecas necesarias utilizando `pip`:

``bash
*pip3 install opencv-python requests numpy*

# Proyecto de Detección de Rostros con OpenCV y DNN

## Descarga de Archivos del Modelo

Descarga los siguientes archivos y colócalos en el mismo directorio que tu script de Python:

| Archivo                                  | Enlace de Descarga                                                                                   |
|------------------------------------------|------------------------------------------------------------------------------------------------------|
| deploy.prototxt                          | [deploy.prototxt](https://github.com/opencv/opencv/raw/3.4.0/samples/dnn/face_detector/deploy.prototxt)|
| res10_300x300_ssd_iter_140000.caffemodel | [res10_300x300_ssd_iter_140000.caffemodel](https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel)|

## Verificación de Archivos

Asegúrate de que los archivos "[deploy.prototxt](https://github.com/opencv/opencv/raw/3.4.0/samples/dnn/face_detector/deploy.prototxt)" y "[res10_300x300_ssd_iter_140000.caffemodel](https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel)" están en el directorio correcto.

### bash
*ls -l*

# Proyecto de Detección de Rostros con OpenCV y DNN

## Uso del Programa

### Ejecución del Script

Guarda el código en un archivo llamado "face_detector.py" y ejecuta el script con el siguiente comando:

### bash
*python3 face_detector.py*

# Proyecto de Detección de Rostros con OpenCV y DNN

## Conclusión

Este proyecto de detección de rostros es una excelente base para diversas aplicaciones que requieren la identificación de rostros. Gracias al uso de modelos DNN preentrenados y la flexibilidad de OpenCV, es posible obtener resultados precisos y eficientes de manera rápida y sencilla.
