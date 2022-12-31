import cv2 as cv
import time
import mediapipe as mp

capture = cv.VideoCapture(0)

mpHands = mp.solutions.hands    
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

previousTime = 0
currentTime = 0


while True:
    sucess, img = capture.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    #print(result.multi_hand_landmarks)
     
    if result.multi_hand_landmarks:
        for EachHandLandmarks in result.multi_hand_landmarks:
            for id, landmarks in enumerate(EachHandLandmarks.landmark):
                #print(id, landmarks)
                height, width, channel = img.shape
                channelX, channelY = int(landmarks.x * width), int(landmarks.y * height)
                #print(id, channelX, channelY)
                #if id == 4:
                #cv.circle(img, (channelX, channelY), 10, (255, 0, 255), cv.FILLED)
            
            mpDraw.draw_landmarks(img, EachHandLandmarks, mpHands.HAND_CONNECTIONS)
        
    
    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime

    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    
    cv.imshow("Image", img)
    cv.waitKey(1)



    

