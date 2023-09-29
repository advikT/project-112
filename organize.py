import os
import shutil

source="/Users/advik/Library/Mobile Documents/com~apple~CloudDocs/Downloads"
destination="/Users/advik/Library/CloudStorage/OneDrive-TroySchoolDistrict"
listoffiles=os.listdir(source)
#print(listoffiles)
for filename in listoffiles:
    name,extension=os.path.splitext(filename)
    print(name)
    print(extension)

    if extension=="":
        continue
    if extension in ['.pdf']:
        path1=source+"/"+filename
        path2=destination+"/"+"pdf files"
        path3=destination+"/"+"pdf files"+"/"+filename
        
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
            
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)
    if extension in ['.heic','.mov','.mp4']:
        path1=source+"/"+filename
        path2=destination+"/"+"video files"
        path3=destination+"/"+"video files"+"/"+filename
        
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
            
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)

