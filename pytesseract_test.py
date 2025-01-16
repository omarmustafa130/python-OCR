import cv2
import pytesseract
import os

os.chdir(r'C://Users/Omarm/Desktop/OCR')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# 1. Loading an image
img = cv2.imread('temp/test1.png')

# 2. Resize the image
#img = cv2.resize(img, None, fx=0.5, fy=0.5) 

# 3. Convert the image to greyscale
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 4. Convert the image to black and white using adaptive threshold
adaptive_thresh = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
text = pytesseract.image_to_string(adaptive_thresh)
print(text)
cv2.imshow('Image', adaptive_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
