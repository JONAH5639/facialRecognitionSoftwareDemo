from cv2 import cv2
import numpy as np

#load Haas classifier
face_cascade = cv2.CascadeClassifier('C:\\Users\jodyb\\OneDrive\\Desktop\\portfolio\\Tkinter_faceApp\\data\\haarcascade_frontalface_alt2.xml')
#Capture video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    #Operations on Frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 2, minNeighbors = 5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_frame = frame[y:y+h, x:x+w]
        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_gray)
        
        #draw square around face
        color = (255, 0, 0) #BGR
        stroke = 4
        end_cord_x = x + w
        end_cord_y = y + h
        cv2. rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
    
    
    #Display frame
    cv2.imshow('Video', frame) #imgshow
    #cv2.imshow('gray', gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()