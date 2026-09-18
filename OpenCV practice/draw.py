import cv2 
import numpy as np
blank = np.zeros((500,500,3), dtype = 'uint8')

#cv2.imshow('Blank',blank)


#painting the blank image with a colour
blank[200:300,300:400] = 0,255,0
cv2.imshow('Color',blank)

cv2.waitKey(0)