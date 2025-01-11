import os
import cv2
import uuid


ANC_PATH = os.path.join('Dataset','rakesh')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    
    frame = frame[120:120+224, 200:200+224, :]
    
    if cv2.waitKey(1) & 0XFF == ord('a'):
        imgname = os.path.join(ANC_PATH,f"{uuid.uuid1()}.jpg")
        cv2.imwrite(imgname, frame)
    
    cv2.imshow('Data Collection', frame)
    
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()