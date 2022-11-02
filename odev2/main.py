# Burak Babaoğlu 02200201066

import cv2
import numpy as np

photo=cv2.imread("odev2foto.jpg",0)
cv2.imshow("fotoduz",photo)              # foto alma
cv2.waitKey()

max_photo=np.max(photo)                   # max değer pixel

[h,w]=np.shape(photo)

for i in range (0,h):
    for j in range (0,w):                     # pixel işlemleri
        photo[i,j]=max_photo-photo[i,j]

cv2.imshow("fototers",photo)                     # foto gösterme
cv2.waitKey()