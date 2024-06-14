## Face Detection Project with OpenCV and DNN

## Description

This project uses the OpenCV library together with a pre-trained Deep Neural Network (DNN) model to detect faces in images. Face detection is a fundamental task in many applications such as security, photography and social networking. This software enables accurate and efficient face detection.

## Features

- Accurate face detection: Uses a pre-trained DNN model to achieve high accuracy in face detection.
- Support for local and online images**: You can process locally stored images or download and process images from URLs.
- Simple interface**: The code is easy to understand and modify, allowing it to be integrated into other projects.

## Advantages and Benefits

| Advantages                    | Benefits                                                     |
|-------------------------------|--------------------------------------------------------------|
| High accuracy                 | Reliable face detection in various conditions                |
| Uses pre-trained models       | No additional training required, ready to use                |
| Support for multiple sources  | Processes images locally and online                          |
| Fácil de usar                 | Clear and well-documented code for easy integration          |

## Installation

### Prerequisites

Before you start, make sure you have the following components installed on your system:

- **Python 3**: If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

### Installing Libraries

Install the necessary libraries using `pip`:


### `bash`
`*pip3 install opencv-python requests numpy*`

## Face Detection Project with OpenCV and DNN

## Model File Download

Download the following files and place them in the same directory as your Python script:

| File                                     | Download link                                                                                        |
|------------------------------------------|------------------------------------------------------------------------------------------------------|
| deploy.prototxt                          | [deploy.prototxt](https://github.com/opencv/opencv/raw/3.4.0/samples/dnn/face_detector/deploy.prototxt)|
| res10_300x300_ssd_iter_140000.caffemodel | [res10_300x300_ssd_iter_140000.caffemodel](https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel)|

## File Verification

Make sure that the files "[deploy.prototxt](https://github.com/opencv/opencv/raw/3.4.0/samples/dnn/face_detector/deploy.prototxt)" y "[res10_300x300_ssd_iter_140000.caffemodel](https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel)" are in the correct directory.

### `bash`
`*ls -l*`

## Face Detection Project with OpenCV and DNN

## Use of the Program

### Running the Script

Save the code in a file called "face_detector.py" and run the script with the following command:

### `bash`
`*python3 face_detector.py*`

## Face Detection Project with OpenCV and DNN

## Conclusion

This face detection project is an excellent basis for various applications that require face identification. Thanks to the use of pre-trained DNN models and the flexibility of OpenCV, accurate and efficient results can be obtained quickly and easily.
