import cv2

# open image
img = cv2.imread('luffy.png')
# check how many channels the image has
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
