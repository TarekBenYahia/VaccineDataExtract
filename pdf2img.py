from pdf2image import convert_from_path
import os


def convertPdf(filename):
    if(filename.split(".")[1]!="pdf"):
        return filename
    imageNotFound = True
    # print("Ahawa file name :", filename)
    while(imageNotFound == True):
        print("Searching for image "+filename)
        # print(os.path.exists("upload/"+filename))
        if(os.path.exists("upload/"+filename)):
            imageNotFound = False
    imageVaccin = convert_from_path("upload/"+filename)
    imageName = ""
    print("En cours")
    for i in range(len(imageVaccin)):
        # Save pages as images in the pdf
        imageName = filename.split(".")[0]
        imageVaccin[i].save('upload/images/'+imageName +
                            '.jpg', 'JPEG')
    return imageName
