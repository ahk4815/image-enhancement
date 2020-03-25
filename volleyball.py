import cv2
import math

def entropy(img):
    no_of_pixel=[0.0 for i in range(256)]
    r, c = img.shape
    for i in range(r):
        for j in range(c):
            no_of_pixel[img[i][j]]=no_of_pixel[img[i][j]] + 1
    no_occ=0
    for i in range(256):
        if no_of_pixel[i]!=0:
            no_occ=no_occ+1
    img_entropy=0.0
    for i in range(256):
        if no_of_pixel[i]!=0:
            l=math.log(no_of_pixel[i],2.0)
            img_entropy=img_entropy + ((no_of_pixel[i]/no_occ)*l)
    return img_entropy


img = cv2.imread('pic2.jpg',0)
ent=entropy(img)
print(ent)

edges = cv2.Canny(img,0,100)

r,c = edges.shape

cnt=0
isum=0
for i in range(r):
    for j in range(c):
        if edges[i][j]!=0:
            cnt=cnt+1
            isum=isum+edges[i][j]

print(cnt)
print(isum)
#cv2.imshow('Edges',edges)
#cv2.waitKey()

