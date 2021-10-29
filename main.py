from pdf2image import convert_from_path
import markRegion
import pytesseract

imageVaccin = convert_from_path("Assets/vaccin.pdf")

print("En cours")
for i in range(len(imageVaccin)):
    # Save pages as images in the pdf
    imageVaccin[i].save('page' + str(i) + '.jpg', 'JPEG')

markRegion.mark_region("page0.jpg")
