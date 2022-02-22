import cv2
import random

img = cv2.imread('assets/bball.jpeg')

# # img returns a numpy array

# print(img.shape)

# #opencv reads as blue green red

# #prints first row of pixels of an image
# # print(img[0])
# # #prints first column of pixels of img
# # print(img[:][0])

# # change all pixels in first 100 rows to random colors
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0,255), random.randint(0,255), 
#             random.randint(0,255)]

# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# copys columns in 30-100 pixels in rows 20 - 200 to put into new image tag
tag = img[20: 100, 30: 100]

#pastes that cut out image into a new location in the image( given rows and columns of pixels)
img[100:180, 90:160] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
