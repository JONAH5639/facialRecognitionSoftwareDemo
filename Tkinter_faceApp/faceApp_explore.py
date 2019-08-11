import tkinter
from cv2 import cv2


class video:
    def __init__(self, window, video_source=0):
        #load Haas classifier
        self.face_cascade = cv2.CascadeClassifier('C:\\Users\\jodyb\\OneDrive\\Desktop\\portfolio\\Tkinter_faceApp\\data\\haarcascade_fullbody.xml')
        #Capture video
        self.cap = cv2.VideoCapture('http://68.175.21.194:8000/mjpg/video.mjpg')

        while True:
            self.ret, self.frame = self.cap.read()

             #Operations on Frame come here
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
    
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor = 1.6, minNeighbors = 5)
            for (x,y,w,h) in faces:
                print(x,y,w,h)
                roi_gray = gray[y:y+h, x:x+w]
                roi_frame = self.frame[y:y+h, x:x+w]
                img_item = "my-image.png"
                cv2.imwrite(img_item, roi_gray)
                
                #draw square around face
                color = (255, 0, 0) #BGR
                stroke = 4
                end_cord_x = x + w
                end_cord_y = y + h
                cv2. rectangle(self.frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
                
            #Display frame
            cv2.imshow('Missing Person Finder', self.frame) #imgshow
        
            if cv2.waitKey(20) & 0xFF == ord('q'):
                self.video.destroy()   
            
        
        
        self.window.mainloop()
        
            
# Create a window and pass it to the Application object
video(tkinter.Tk(), "Tkinter and OpenCV")