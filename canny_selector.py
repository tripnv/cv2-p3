#import opencv and numpy
import cv2  
import numpy as np

#trackbar callback fucntion to update HSV value
def callback(x):
    global minVal, maxVal, apertureS
    #assign trackbar position value to H,S,V High and low variable
    minVal = cv2.getTrackbarPos('minVal','controls')
    maxVal = cv2.getTrackbarPos('maxVal','controls')
    apertureS = cv2.getTrackbarPos('Aperture', 'controls')



#create a seperate window named 'controls' for trackbar
cv2.namedWindow('controls',2)
cv2.resizeWindow("controls", 550,10);


#global variable
minVal = 0
maxVal = 180


#create trackbars for high,low H,S,V 
cv2.createTrackbar('minVal','controls',0,255, callback)
cv2.createTrackbar('maxVal','controls',255,255, callback)


input_path = input()
img=cv2.imread(input_path)

while(1):
    #read source image

    #convert sourece image to HSC color mode
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #
    min_val, max_val, ap = minVal, maxVal, apertureS

    #making mask for hsv range
    mask = cv2.Canny(img, min_val, max_val, apertureSize = 3)

    #show image
    cv2.imshow('mask',mask)

    #waitfor the user to press escape and break the while loop 
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
        
#destroys all window
cv2.destroyAllWindows()
