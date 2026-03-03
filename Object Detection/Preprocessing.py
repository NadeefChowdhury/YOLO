import os
import cv2

path = "D:/Python codes/YOLO Cat/cat/images/"

#OTHER PRE PROCESSINGS: RESIZE, BLUR, BINARY THRESHOLDING

files = os.listdir(path)

for file in files:
    
    if file.endswith(('.jpg', '.png', 'jpeg')):
        img_path = path + file
        image = cv2.imread(img_path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        dst = cv2.equalizeHist(gray)
        cv2.imwrite("D:/Python codes/YOLO Cat/cat2/images/"+file, dst)
        # load file as image...





