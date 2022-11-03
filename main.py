import cv2
img=cv2.imread("poster.jpg")
rocket=img[120:360,400:500]
img[0:240,500:600]=rocket
texttoshow="Hello World!"
cv2.putText(img,texttoshow,(20,220),fontFace=cv2.FONT_ITALIC,fontScale=1,color=(0,0,255))
cv2.imshow("Hello World!",img)
cv2.waitKey(0)