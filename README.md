# SLAM-project_Data-set-building
This repository converts raw data from Realsense D435i camera into dataset that can be imported to ORBSLAM2 system

Realsense D435i can export color data and depth data in a json format(hierarchy dictionary).
This repository can convert that kind of data into a dataset which can be imported into SLAM system.

hex2bgr.py converts hex arrays of the json format *.txt file into bgr format and create a *.json file
hex2z16.py converts hex arrays of the json format *.txt file into z16 format and create a *.json file

color_convertion.py and depth_convertion.py convert the respective *.json file into images

image.txt file converts the depth and color images into depth.txt and image.txt in a time sequence order

associate.py can associate the depth.txt and image.txt
