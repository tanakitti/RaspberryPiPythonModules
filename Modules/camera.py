import cv2

# initialize the camera
cam = cv2.VideoCapture(0)

# get width and height
w = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)


def takePicture(filename):
    # get picture from the webcam
    ret, image = cam.read()
    if ret:
        # save picture
        cv2.imwrite(filename,image)
        print("Save completely"+filename+"("+str(w)+"X"+str(h)+")")
    cam.release()

# test module
if __name__ == '__main__':
    takePicture("../test.jpg")