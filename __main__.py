import cv2 as cv

img = cv.imread("hereimg.png")



def convertBGR2GS(source_img):
    img_gs = cv.cvtColor(source_img, cv.COLOR_BGR2GRAY);
    return img_gs

cv.imshow('readimage.png',img)
cv.imshow('gsimage.png',convertBGR2GS(img))

gsimage = convertBGR2GS(img)

ret, thresh = cv.threshold(gsimage, 127, 230, cv.THRESH_BINARY)

cv.imshow('thresh', thresh)

canny = cv.Canny(gsimage, 0,254)
cv.imshow('Canny Edges', canny)


cv.waitKey(0)