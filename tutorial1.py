import cv2

img = cv2.imread('assets/bball.jpeg')
# changes x y of img by factor fx fy
img = cv2.resize(img, (0, 0), fx=2.0, fy = 2.0)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

# writes new image to new file
cv2.imwrite('new_img.jpg', img)

# -1, cv2.IMREAD_COLOR : Loads a color image. Any transparancy of image will not appear
# 0, cv2.IMREAD_GRAYSCALE : loads image in grayscale
# 1, cv2.IMREAD_UNNCAHGED: loads a color image with transparnecy(all normal)

#displays image in img variable
cv2.imshow('Image',img)
cv2.waitKey(0) # wait inf time to press any key ( then continue this line) > 0 means wait for that many millisecond
cv2.destroyAllWindows()