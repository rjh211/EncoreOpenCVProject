from cv2 import cv2
import math

def CalDistance(lst):
    return (lst[2] ** 2 + lst[3] ** 2)**0.5

image = cv2.imread('../playdata/Python_encore/EncoreOpenCVProject/Image/ratate150.jpg',cv2.IMREAD_GRAYSCALE)
_, binaryImage = cv2.threshold(image,0,255,cv2.THRESH_OTSU)
minArea = 40001
lst = [0,0,0,0]
nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(binaryImage)
for i in range(nlabels):
    if i < 5:
        continue
    area = stats[i, cv2.CC_STAT_AREA]
    left = stats[i, cv2.CC_STAT_LEFT]
    top = stats[i, cv2.CC_STAT_TOP]
    width = stats[i, cv2.CC_STAT_WIDTH]
    height = stats[i, cv2.CC_STAT_HEIGHT]
    
    if area > 50 and area < minArea:
        minArea = area
        lst = [left, top, width, height]
degree = -lst[3] / CalDistance(lst) if lst[0] + 0.5 * lst[2] < 100 else lst[3] / CalDistance(lst)
MOH = lst[1] + 0.5 * lst[3]
MOW = lst[0] + 0.5 * lst[2]
if MOH < 100 and MOW < 100 : #2사분면
    degree = -math.asin(lst[3] / CalDistance(lst))
elif MOH < 100 and MOW >= 100 : #1사분면
    degree = math.asin(lst[3] / CalDistance(lst))
elif MOH > 100 and MOW < 100 : #3사분면
    degree = math.asin(lst[3] / CalDistance(lst))
else : #4사분면
    degree = math.asin(lst[3] / CalDistance(lst))
print(degree)