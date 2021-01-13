import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 270)

while(True):
    # Capture frame by frame
    ret, frame = cap.read()

    # converts image to grayscale and applies binary threshold
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    ret, thres = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

    # Display the resulting frame
    cv.imshow('frame', thres)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv.destroyAllWindows()
