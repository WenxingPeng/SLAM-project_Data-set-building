# -*- coding: utf-8 -*-   
import time     
import os  
import shutil
 
 
def readFilename(path,allfile): # this function returns all the file name in the path
    filelist = os.listdir(path) # list the file and foders in the directory and return the filesname list
    filelist.sort()
    for filename in filelist:
        filepath = os.path.join(path, filename) # merge the path and filename into  a new path
        if os.path.isdir(filepath):
            readFilename(filepath, allfile)
        else:                      # if filepath is a file
            allfile.append(filepath)
    return allfile
 
 
 
if __name__ == '__main__':
    # open rgb file and read color images
    path1='/home/wenxing/OneDrive_2020-08-05/SLAMDATASET/rgb/' 
    allfile1=[]
    allfile1=readFilename(path1,allfile1)
    txtpath1='/home/wenxing/OneDrive_2020-08-05/SLAMDATASET/' + 'rgb.txt' 
    # write notes
    with open(txtpath1,'a+') as fp:
        fp.write("# color image"+'\n')
        fp.write("# timestamp filename"+'\n')
    
    # open depth file and read depth images
    path2='/home/wenxing/OneDrive_2020-08-05/SLAMDATASET/depth/' 
    allfile2=[]
    allfile2=readFilename(path2,allfile2)
    txtpath2='/home/wenxing/OneDrive_2020-08-05/SLAMDATASET/' + 'depth.txt' 
    # write notes
    with open(txtpath2,'a+') as fp:
        fp.write("# depth image"+'\n')
        fp.write("# timestamp filename"+'\n')

    
    for name1 in allfile1:
        print('name1: ',name1)  # print file name
        file_pfx1=name1.split("/")[-1].split(".")[-1] # postffix
        file_name1=name1.split("/")[-1].split(".")[-3]+'.'+name1.split("/")[-1].split(".")[-2] #timestamp
        txt_name1='rgb/' + name1.split("/")[-1]
        print('timestamp: ',file_name1)
        if file_pfx1=='png':
            print(name1.split("/")[-1])
            print(file_name1)
            with open(txtpath1,'a+') as fp:
                fp.write("".join(file_name1 + " " + txt_name1)+"\n")

    for name2 in allfile2:
        #print(name2)  # print file name
        file_pfx2=name2.split("/")[-1].split(".")[-1] # postffix of file
        file_name2=name2.split("/")[-1].split(".")[-3]+'.'+name2.split("/")[-1].split(".")[-2] #timestamp
        txt_name2='depth/' + name2.split("/")[-1]
        if file_pfx2=='png':
            #print(name2.split("/")[-1])
            #print(file_name2)
            with open(txtpath2,'a+') as fp:
                fp.write("".join(file_name2 + " " + txt_name2)+"\n")
   