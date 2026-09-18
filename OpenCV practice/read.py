import cv2 as cv

#Reading an Image

img = cv.imread("TheBlackPearl.jpeg")

cv.imshow("The Black Pearl",img)

cv.waitKey(0)

#Reading a video

vid = cv.VideoCapture("Video.mov")

while True:
    isTrue, frame = vid.read()

    cv.imshow("ME-E-E",frame)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

vid.release()
cv.destroyAllWindows()
