import cv2
import numpy as np


def yazdir(histogram):
    for k in range (0,256):
        print(k,"=",histogram[k])


img = cv2.imread('apple.jpeg',0)


histogram= np.zeros(256)
[h,w]=np.shape(img)
for i in range (0,h):
    for j in range (0,w):
        k=img[i,j]
        histogram[k]=histogram[k]+1

yazdir(histogram)
cv2.imshow("grey",img)
cv2.waitKey()