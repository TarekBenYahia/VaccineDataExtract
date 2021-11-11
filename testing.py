import cv2
import pytesseract
import numpy as np
from pyzbar.pyzbar import decode
from pdf2img import convertPdf
from pprint import pprint
from itertools import islice


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def nth_index(iterable, value, n):
    matches = (idx for idx, val in enumerate(iterable) if val == value)
    return next(islice(matches, n-1, n), None)


def testing(file):
    imgName = convertPdf(file)
    image = 'upload/images/'+imgName+".jpg"
    print("image path is : ", image)
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

    # print(dict)
    # Evax number = 16
    dateDose2 = []
    if(words[words.index('vaccin:')+1] != 'JENSSEN'):
        dateDose2 = words[words.index('2:')+1:words.index('N°')]
    wordsDict = {
        "numEvax": words[words.index("EVAX:")+1],
        'nomEtPrenom': words[words.index('Prénom:')+1:words.index('Carte')],
        'idNumber': words[words.index("nationale:")+1],
        'dateOfBirth': words[words.index("naissance:")+1:nth_index(words, "Informations", 2)],
        'refVaccin': words[words.index(':')+1],
        'nomDeVaccin': words[words.index('vaccin:')+1],
        'dateDose1': words[words.index('1:')+1:nth_index(words, 'Date', 3)],
        'dateDose2': dateDose2,
    }

    pprint(wordsDict)
    print(words)
    return({"dict": dict, "words": wordsDict})

    # dict = eval(code[0].data.decode('UTF-8'))
    # print(dict)
    # cv2.imshow('Result', img)
    # cv2.waitKey(0)
