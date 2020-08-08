'''
this function is used to convert the hex string into *.json files from given raw data
first to execute
'''

import os
import json
import numpy as np
path_file = os.path.dirname(os.path.abspath(__file__))
class_path = os.path.join(path_file, "/home/wenxing/OneDrive_2020-08-05/SLAMDATASET/realsensedata.txt")
 
with open(class_path, "r", encoding="gbk") as fileopen:
     line_rd = fileopen.read()
     line_rd=line_rd.replace("'",'"')
     realsense_dict = json.loads(line_rd)



# format conversion
for i in realsense_dict.keys():
    b = bytearray.fromhex(realsense_dict[i]["color"]["colorData"])
    c=list(b)
    d=np.reshape(c,(240,320,3))
    e=d.tolist()
    realsense_dict[i]["color"]["colorData"]=e

#print(realsense_dict["2"]["color"]["colorData"])

realsense_color={}
for i in realsense_dict.keys():
     IMAGE_NAME = realsense_dict[i]["color"]["timeStamp"]
     realsense_color[IMAGE_NAME] = realsense_dict[i]["color"]["colorData"]

data=json.dumps(realsense_color)
fileObject=open('realsense_color.json','w')
fileObject.write(data)
fileObject.close()




