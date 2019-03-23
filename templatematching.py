# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:07:55 2019

@author: chen
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('B1.jpg',0)
template = cv2.imread('template-B1.jpg',0)
w, h = template.shape[::-1]
print(w,h)
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = min_loc
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
#print(top_left,bottom_right)
cv2.rectangle(img,top_left, bottom_right, (0,0,255), 2)

plt.subplot(121),plt.imshow(res,cmap = 'winter_r')
plt.title('Matching Result'), plt.xticks(), plt.yticks([])

plt.subplot(122),plt.imshow(img,cmap = 'pink')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()