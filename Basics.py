import cv2
import numpy as np
import face_recognition

imgYange = face_recognition.load_image_file('imagesBasic/Yange.jpg')
imgYange = cv2.cvtColor(imgYange, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('imagesBasic/YangeTest.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgYange)[0]
encodeYange = face_recognition.face_encodings(imgYange)[0]
cv2.rectangle(imgYange,(faceLoc[3], faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3], faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(0,200,0), 2)

results = face_recognition.compare_faces([encodeYange], encodeTest)
faceDis = face_recognition.face_distance([encodeYange], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0],2)}', (50,130),cv2.FONT_HERSHEY_COMPLEX,1, (0,200,0), 2)

cv2.imshow('YangeTest',imgTest)
cv2.imshow('Yange',imgYange)
cv2.waitKey(0)