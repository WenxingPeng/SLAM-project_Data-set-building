'''
this function is used to convert the hex string into *.json files from given raw data
first to execute
'''

import os
import json
import numpy as np
path_file = os.path.dirname(os.path.abspath(__file__))
class_path = os.path.join(
    path_file, "/home/wenxing/OneDrive_2020-08-05/MSC_Project_Data/realsensedata.txt")

with open(class_path, "r", encoding="gbk") as fileopen:
    line_rd = fileopen.read()
    line_rd = line_rd.replace("'", '"')
    realsense_dict = json.loads(line_rd)
'''c=[]
for j in range(0,len(realsense_dict['0']["depth"]["depthData"]),4):
         c.append(int(realsense_dict['0']["depth"]["depthData"][j:j+4],16))
d=np.reshape(c,(240,320))
print(d)'''

# format conversion
for i in realsense_dict.keys():
     c=[]
     for j in range(0,len(realsense_dict[i]["depth"]["depthData"]),4):
         c.append(int(realsense_dict[i]["depth"]["depthData"][j:j+4],16))
     d=np.reshape(c,(240,320))
     e=d.tolist()
     realsense_dict[i]["depth"]["depthData"]=e


realsense_depth={}
for i in realsense_dict.keys():
    IMAGE_NAME = realsense_dict[i]["depth"]["timestamp"]
    realsense_depth[IMAGE_NAME] = realsense_dict[i]["depth"]["depthData"]

data=json.dumps(realsense_depth)
fileObject=open('realsense_depth.json','w')
fileObject.write(data)
fileObject.close()
