import cv2
import numpy

resim=cv2.imread("adile.jpg")
aynalananResim=cv2.copyMakeBorder(resim,75,75,125,125,cv2.BORDER_REFLECT)
uzatilanResim=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE)
tekraredenResim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)
sarilanResim=cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT,value=(0,0,255))
cv2.imshow("Adile Nasit",aynalananResim)
cv2.imshow("Adile Nasit",uzatilanResim)
cv2.imshow("Adile Nasit",tekraredenResim)
cv2.imshow("Adile Nasit",sarilanResim)

cv2.waitKey(0)
cv2.destroyAllWindows()
