from cv2 import cv2

niddleImg = cv2.imread('../playdata/Python_encore/EncoreOpenCVProject/Image/orgClock.jpg',cv2.IMREAD_GRAYSCALE)
height, width = niddleImg.shape
for i in range(1, 13):
    matrix = cv2.getRotationMatrix2D((width/2, height/2), i*30, 1)
    dst = cv2.warpAffine(niddleImg, matrix, (width, height))
    cv2.imwrite('ratate' + str(i*30)+'.jpg',dst)