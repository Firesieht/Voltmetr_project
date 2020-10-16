import cv2
import numpy as np


def nothing(x):
    pass


# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h, s, v = 100, 100, 100

# Creating track bar
cv2.createTrackbar('min_h', 'result', 0, 255, nothing)
cv2.createTrackbar('min_s', 'result', 0, 255, nothing)
cv2.createTrackbar('min_v', 'result', 0, 255, nothing)

cv2.createTrackbar('max_h', 'result', 0, 255, nothing)
cv2.createTrackbar('max_s', 'result', 0, 255, nothing)
cv2.createTrackbar('max_v', 'result', 0, 255, nothing)
frame = cv2.imread("1.png")
#hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
cam = cv2.VideoCapture(0)
hsv = frame
while 1:
    _, frame = cam.read()
    # converting to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # get info from track bar and appy to result
    min_h = cv2.getTrackbarPos('min_h', 'result')
    min_s = cv2.getTrackbarPos('min_s', 'result')
    min_v = cv2.getTrackbarPos('min_v', 'result')

    max_h = cv2.getTrackbarPos('max_h', 'result')
    max_s = cv2.getTrackbarPos('max_s', 'result')
    max_v = cv2.getTrackbarPos('max_v', 'result')

    # Normal masking algorithm
    lower_blue = np.array([min_h, min_s, min_v])
    upper_blue = np.array([max_h, max_s, max_v])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow("mask", mask)



    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
