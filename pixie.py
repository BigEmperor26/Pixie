import cv2

# open image
img = cv2.imread('luffy.png')
# check the colorspace
print(img.dtype)
# check how many channels the image has
print(img.shape)
