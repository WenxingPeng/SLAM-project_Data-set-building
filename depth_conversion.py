from cv2 import cv2
import numpy as np
import json

# *.json file name
JSON_NAME = 'realsense_depth.json'


# convert to images
# read file as dictionart
with open(JSON_NAME, "rb") as json_file:
    img_dict = json.load(json_file)

for frame in img_dict.keys():
    img_list = img_dict[frame]
    img = np.asarray(img_list)
    # convert 16 bits images to 8 bits
    max_v = img.max()
    min_v = img.min()
    img = (img - min_v)*255 /(max_v - min_v)
    
    IMAGE_NAME = "depth/"+frame + ".png"
    cv2.imwrite(IMAGE_NAME,img)