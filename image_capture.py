"""
ELEKTRON © 2022
Written by Nilusink and melektron
www.elektron.work
30.09.22, 13:57

Module to handle capturing screenshots from the external video device
"""

import os
import cv2

DEVICE_ID = 0

camera = cv2.VideoCapture(DEVICE_ID)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
#camera.set(cv2.CAP_PROP_FORMAT, -1)


def take_picture(x=1920, y=1080, format="yuyv422", file="/tmp/out1.png") -> str:
    return_value, image = camera.read()
    cv2.imwrite(file, image)
    #os.system(f"ffmpeg -f v4l2 -video_size {x}x{y} -input_format {format} -i /dev/video{DEVICE_ID} -frames 1 {file}")
    return file

# take one picture and remove it again to prime the pipeling
os.system(f"rm {take_picture()}")