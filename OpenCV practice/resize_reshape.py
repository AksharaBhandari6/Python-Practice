import cv2 as cv

img = cv.imread('img.jpg')
#creating a func to rescale
def rescaleFrame(frame,scale = 0.75):
    width = int(frame.shape[1] * scale ) #[1] is for the width
    height = int(frame.shape[0] * scale) #[0] is for the height

    dimensions = (width , height) #a tuple created for both the dimensions

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


cv.imshow('The black pearl', img)
cv.imshow('The black pearlieeee',rescaleFrame(img))

cv.waitKey(0)
cv.destroyAllWindows()