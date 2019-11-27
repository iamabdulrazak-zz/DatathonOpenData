import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

pdf = wi(filename = "pdfTest.pdf", resolution = 300)
pdfImage = pdf.convert('jpeg')

ImageBlobs = []

for img in pdfImage.sequence:
    imaPage = wi(image=img)
    ImageBlobs.append(imaPage.make_blob('jpeg'))

recognized_text = []

for ImageBlob in ImageBlobs:
    im = Image.open(io.BytesIO(ImageBlob))
    text = pytesseract.image_to_string(im, lang = 'eng')
    recognized_text.append(text)
    
print(recognized_text)