import cv2 as cv 


img1_path = "img/cat.jpg"
img2_path = "img/dog.jpg"

original_img1 = cv.imread(img1_path)
original_img2 = cv.imread(img2_path)

original_img1 = cv.resize(original_img1, dsize=(640, 480), interpolation=cv.INTER_AREA)
original_img2 = cv.resize(original_img2, dsize=(640, 480), interpolation=cv.INTER_AREA)

# 변환 처리: 이미지 덧셈/곱셈
alpha = 0.6
beta = 0.7

# add_img1 = original_img1 + original_img2
add_img1 = cv.add(original_img1, original_img2)
# add_img2 = original_img1 * 0.5 + original_img2 * 0.5
add_img2 = cv.add(original_img1 * 0.5, original_img2 * 0.5)
add_img3 = original_img1 * alpha + original_img2 * (1-alpha)
add_img4 = cv.addWeighted(original_img1, alpha, original_img2, beta, 0.0)


cv.imshow('Original', original_img1)
cv.imshow('Original', original_img2)
cv.imshow('Add', add_img1)
cv.imshow('Add 50%', add_img2)
cv.imshow('Add 60:40', add_img3)
cv.imshow('Add Weighted 60:70', add_img4)


cv.waitKey(0)
cv.destroyAllWindows()
