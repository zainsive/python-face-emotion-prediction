from deepface import DeepFace
import cv2 as cv


image_name = input("Enter the file name with extension: ")
readed_img = cv.imread(image_name)


analysis = DeepFace.analyze(readed_img, actions = ["age", "gender", "emotion", "race"])

font = cv.FONT_HERSHEY_SIMPLEX

cv.putText(readed_img,"Age: "+str(analysis['age']),(0,20),font,0.5,(255,255,255),1)
cv.putText(readed_img,"Gender: "+str(analysis['gender']),(0,40),font,0.5,(255,255,255),1)
cv.putText(readed_img,"Emotion: "+str(analysis['dominant_emotion']),(0,60),font,0.5,(255,255,255),1)
cv.putText(readed_img,"Race: "+str(analysis['dominant_race']),(0,80),font,0.5,(255,255,255),1)

cv.imshow('image', readed_img)

cv.waitKey(0)

cv.destroyAllWindows()