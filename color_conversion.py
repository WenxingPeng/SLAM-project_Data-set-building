#read string from *.json and convert it to images
# coding: utf-8
from cv2 import cv2
import numpy as np
import json

# *.json file name
JSON_NAME = 'realsense_color.json'

# convert to images
# read file as dictionary
with open(JSON_NAME, "rb") as json_file:
    img_dict = json.load(json_file)

for frame in img_dict.keys():
    img_list = img_dict[frame]
    # list to ndarray
    img = np.asarray(img_list)
    IMAGE_NAME = "rgb/"+frame + ".png"
    cv2.imwrite(IMAGE_NAME,img)
