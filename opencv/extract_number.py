import pytesseract
import cv2

img = cv2.imread("./resource/IMG_0185.jpeg")
res = pytesseract.image_to_string(img)
print(res)
