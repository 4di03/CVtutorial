import numpy as np
import cv2
#load both in as grayscale for algorithm
img = cv2.imread('assets/soccer_practice.jpeg', 0)
img = cv2.resize(img, (0,0), fx = 0.8, fy = 0.8)
#image we will be looking for 
template = cv2.imread('assets/shoe.PNG', 0)
template = cv2.resize(template, (0,0), fx = 0.8, fy = 0.8)

# if you resize main immage, need to resize template as well

# no 3rd dimensions cause grayscale is represnted in one integer
h,w = template.shape

#methods for template matching (try for best ones)
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

#try all methods
for method in methods:
    #new image to draw box over
    img2 = img.copy()

    #returns array of numvers indicating how well the template fits in that region
    result = cv2.matchTemplate(img2, template, method)

    #returns correpsond mins and mmax of vlaues and locatiosn of result
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else: 
        location = max_loc

    #drawing rectangle to fit around template spot
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)

    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # dimension of result: (W - w + 1, H - h + 1) 
    #   product of two values represnts number of possible slides of image
