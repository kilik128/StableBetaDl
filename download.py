import sys
import os
import requests
import cv2
import glob
from PIL import Image


print('Argument:', sys.argv[1])

alltxt = glob.glob( "D:\\Center\\txt\\" + '/*.txt')
print(str( len(alltxt)))
i = int(sys.argv[1])
print(alltxt[i])
print(alltxt[i].split("\\")[-1])
cc =alltxt[i].split("\\")[-1]
file = open(alltxt[i], encoding="utf8")
export  = "D:\Center\PNG\\PNG"+cc+"\\"
exportjpg  = "D:\Center\export\\JPG"+cc+"\\"

try: 
    os.mkdir(export)
except OSError as error: 
    print(error)

try: 
    os.mkdir(exportjpg)
except OSError as error: 
    print(error)  

text = file.read().splitlines()
print(str( len(text)))
for i in range(0,len(text)):
          #print(text[i])
          #print(text[i].split("/")[-1])
          print(str(i))
          url = text[i]
          name = text[i].split("/")[-1]
          if (text[i][0] == "h"):
             if (os.path.exists(exportjpg +name+".jpg")== False):
                r = requests.get(url, allow_redirects=True)
                open(export+name, 'wb').write(r.content)
                #png_img = cv2.imread(export+name)
                #cv2.imwrite(exportjpg +name+".jpg", png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
                if (os.path.exists(exportjpg +name)== True):
                  img_PIL = Image.open((export+name))
                  img_PIL.save(exportjpg +name+".jpg")
