import cv2
import face_recognition as fr

cam = cv2.VideoCapture(0)
cv2.namedWindow("Screenshot")
img_counter=0
while(True):
    ret,frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow("Test",frame)
    k  = cv2.waitKey(1)
    if(k == ord("a")):
        print("Closing app")
        break
    elif(k == ord("c")):
        img_name = "C:/Users/Mk1sh/Downloads/face_recognition/images/open_cv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        print("SC taken")
        img_counter+=1
cam.release()
cam.destroyAllWindows()