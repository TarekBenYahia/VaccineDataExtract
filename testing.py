import cv2
import pytesseract
import numpy as np
from pyzbar.pyzbar import decode


pytesseract.pytesseract.tesseract_cmd = 'D:\\Program Files\\Tesseract-OCR\\tesseract.exe'


image = 'page0.jpg'
img = cv2.imread(image)
img2Decode = img
# img = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)

heightImg, widthImg, _ = img.shape
boxes = pytesseract.image_to_data(img)
words = []
for x, b in enumerate(boxes.splitlines()):
    # print(b)
    if x != 0:
        b = b.split()
        # print(b)
        if(len(b) == 12):
            words.append(b[11])
            x, y, width, height = int(b[6]), int(
                b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (width+x, height+y), (0, 0, 255), 3)
            cv2.putText(img, b[11], (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)


code = decode(img2Decode)

qrContent = str(code[0].data.decode('UTF-8'))

values = qrContent.split(',')

values[0] = values[0][1:]
values[-1] = values[-1][:-1]

dict = {}

for value in values:
    value = value.replace('"', '')
    # print(value)
    dict[value[:value.index(':')]] = value[value.index(':')+1:]
# print(values)
print(dict)
print(words)

# dict = eval(code[0].data.decode('UTF-8'))
# print(dict)
cv2.imshow('Result', img)
cv2.waitKey(0)
