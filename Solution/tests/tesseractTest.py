from PIL import Image
import pytesseract

def extractWords():
    img1 = Image.open("Solution\images\img1.jpg")
    img2 = Image.open("Solution\images\img2.jpg")
    engText = pytesseract.image_to_string(img1, lang='eng')
    araText = pytesseract.image_to_string(img2, lang='ara')
    print(engText)
    print(araText)

extractWords()
