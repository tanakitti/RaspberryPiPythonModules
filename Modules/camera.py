import cv2

# initialize the camera
cam = cv2.VideoCapture(0)
w = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)


def takePicture(filename):
    ret, image = cam.read()
    if ret:
        cv2.imwrite(filename,image)
        print("Save completely"+filename+"("+str(w)+"X"+str(h)+")")
    cam.release()