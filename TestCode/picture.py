import cv2

# initialize the camera
cam = cv2.VideoCapture(0)
w = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(w,h)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
w = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(w,h)
ret, image = cam.read()




if ret:
    print("Oh Yeah")
    #cv2.imshow('SnapshotTest',image)
    #cv2.waitKey(0)
    #cv2.destroyWindow('SnapshotTest')
    #cv2.imwrite('/Users/bank21235/Documents/Senior_Project/SnapshotTest.jpg',image)
    cv2.imwrite('/home/pi/Documents/pyscripts/BankWS/SnapshotTest.jpg',image)
cam.release()
