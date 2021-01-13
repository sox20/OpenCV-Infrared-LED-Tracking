import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
#cap.set(3, 480)
#cap.set(4, 270)

while(True):
    # Capture frame by frame
    ret, frame = cap.read()
    
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    
    mask = cv.inRange(gray, 240, 255)
    mask = cv.blur(mask, (6,6))
    
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2:]
    
    tracked_contours = []
    
    for i in contours:
        x, y, w, h = cv.boundingRect(i)
        # checks min and max area and checks how "sqaure" the bounding box
        if cv.contourArea(i) <= 3000.0 and cv.contourArea(i) > 150 and w/h < 1.2 and w/h > 0.8:
            tracked_contours.append(i)
            
    for i in tracked_contours:
        x, y, w, h = cv.boundingRect(i)
        
        # render bounding box
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
        # render circle at center of bounding box
        cv.circle(frame, (x + int(w/2), y + int(h/2)), 4, (255, 0, 0), -1)
    
    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv.destroyAllWindows()
