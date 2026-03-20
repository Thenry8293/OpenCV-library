import cv2 as cv
import numpy as np

osu_img = cv.imread('demoImages\\download.jpg', cv.IMREAD_UNCHANGED)
circle_img = cv.imread('demoImages\\download(1).jpg', cv.IMREAD_UNCHANGED)

needle_w = circle_img.shape[1]
needle_h = circle_img.shape[0]

result = cv.matchTemplate(osu_img, circle_img, cv.TM_CCOEFF_NORMED)
print(result)

threshold = 0.7
locations = np.where(result >= threshold)
# print(locations)

locations = list(zip(*locations[::-1]))
# print(locations)

rectangles = []
for loc in locations:
    rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
    rectangles.append(rect)


cv.groupRectangles(rectangles, 1, 0.5)
print(rectangles)

if len(rectangles):
    print('Found a match!')

    needle_w = circle_img.shape[1]
    needle_h = circle_img.shape[0]
    line_color = (0,255,0)
    line_type = cv.LINE_4
    

    for (x, y, w, h) in rectangles:
        top_left = (x, y)
        bottom_right = (x + w, y + h)

        cv.rectangle(osu_img, top_left, bottom_right, line_color, line_type,)

    cv.imshow('Result', osu_img)
    cv.waitKey()
else:
    print('No match found.')







# Get the best match position/confidence from the result/show rectangle in img
# min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

# print('Best match top left position: %s' % str(max_loc))
# print('Best match confidence: %s' % max_val)

# threshold = 0.7
# if max_val >= threshold:
#     print('Found a match!')

#     needle_w = circle_img.shape[1]
#     needle_h = circle_img.shape[0]

#     top_left = max_loc
#     bottom_right = top_left[0] + needle_w, top_left[1] + needle_h

#     cv.rectangle(osu_img, top_left, bottom_right, (0,255,0), thickness = 2, lineType = cv.LINE_4)

#     cv.imshow('Result', osu_img)
#     cv.waitKey()
# else:
#     print('No match found.')
