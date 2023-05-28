import cv2
import time
import numpy as np
import HandTrackingModule as htm    
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

"""
cihazda kamera hangi indexte onu bulmak için Not: laptop ise genelde 0 masaüstü harici kamera ise 1
for i in range(10):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera index: {i} is open")
    else:
        print(f"Camera index: {i} is not open")
    cap.release()
"""
wCam, hCam=640,480

cap =cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0 

detector = htm.handDetector(detectionCon=0.7)
#pycaw  windows ses sistemi için python kütüphanesi

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0
#print(volume.GetVolumeRange())  #Volume range hesaplamak için

while True:
    success,img =cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False) 
    
    if len(lmList) != 0:
        #elimizin hangi bölgeleri arasından volume belirlemek istiyorsak (ben 4 .ve 8. bölgeyi seçtim baş ve işaret parmak uçları) mediapipe kütüphanesini inceleyerek el bölgelerine bakabilirsiniz.
        #print(lmList[4], lmList[8])

        #el uçlarına iki nokta koyarak belirleme mediapipe kütüphanesinden çekiyoruz 4. ve 8. noktaları
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        #iki nokta arası düz bir çizgi çekip volume ayarlamak için
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        #iki noktanın ortasına bir nokta ekliyoruz
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1) #Hand range hesaplamak için
        #print(length) #en yüksek ve en düşük aralığı bulmak için loglayınız
        #benim elime göre ayarladığımda min 20 max 180
        # Hand range 20 - 180
        # Volume Range -63 min  max -0.1 

        vol = np.interp(length, [20, 180], [minVol, maxVol])
        volBar = np.interp(length, [20, 180], [400, 150])
        volPer = np.interp(length, [20, 180], [0, 100])
        #print(int(length),vol)
        volume.SetMasterVolumeLevel(vol,None)

        if length < 20:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
 
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)
 
      

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img, f'FPS:{int(fps)}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)

    cv2.imshow("Img",img)
    cv2.waitKey(1)