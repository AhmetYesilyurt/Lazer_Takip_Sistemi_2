import cv2
import RPi.GPIO as GPIO

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 3)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
    #Yüzü kare içine aldıktan sonra, karenin merkezini bulma
        x_eksen=x+(w/2)
        y_eksen=y+(h/2)
        print ("[",int(x_eksen),int(y_eksen),"]")


        # Kullandığımız ekran boyutumuz 640x480
        #Görüntünün merkez noktası ise (320,240)
        #Motorları hareket ettirmek için L298N motor sürücüsüne sinyal yolluyuruz
        if(x_eksen < 320):
            GPIO.wait_for_edge(24, GPIO.RISING)
            GPIO.wait_for_edge(23, GPIO.FALLING)
        if(x_eksen > 321):
            GPIO.wait_for_edge(23, GPIO.RISING)
            GPIO.wait_for_edge(24, GPIO.FALLING)

        if(y_eksen < 240):
            GPIO.wait_for_edge(25, GPIO.RISING)
            GPIO.wait_for_edge(26, GPIO.FALLING)
        if(y_eksen > 241):
            GPIO.wait_for_edge(26, GPIO.RISING)
            GPIO.wait_for_edge(25, GPIO.FALLING)

        
        cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

