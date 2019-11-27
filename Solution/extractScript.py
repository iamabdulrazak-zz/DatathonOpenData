from PIL import Image
import pytesseract
import cv2
from glob import glob
import glob

path = "Solution\images\*.*"
nutList = ["Carbohydrate","Energy","energy","Total Fat","total Fat","Total fat","total fat","saturated fat","Saturated Fat","saturated Fat","Saturated fat", "monounsaturated fat","monounsaturated Fat",
"Monounsaturated Fat","Monounsaturated fat","polysaturated fat","Polysaturated Fat","Polysaturated fat","Polysaturated Fat","trans fat","trans Fat","Trans Fat","Trans fat","cholestrol","Cholestrol","sodium",
"Sodium","Total Carbohydrate","Total carbohydrate","total Carbohydrate","total carbohydrate","dietary fiber","Dietary fiber","dietary Fiber","Dietary Fiber","sugar", "Sugar","protein",
"Protein","Vitamin C","Vitamin c","vitamin C","vitamin c","Calcium","iron","Iron","calories","Calories","total sugars","Total Sugars","Total sugars","total Sugars", "potassium","Potassium","Fat",
"fat","Saturated","saturated","Trans","trans","carbohydrate","Carbohydrate","sugars","Sugars", "added sugars","added sugar","Added Sugar",
"Added sugar","added Sugar","salt","Salt","vitamin d","vitamin D","Vitamin d","Vitamin D","vitamin a","vitamin A","Vitamin a","Vitamin A" ]
dataset = ""

for file in glob.glob(path):
    image_id=""
    counter = 0
    for position, name in enumerate(file):
        if "/" == file[position] :
            counter += 1
        if counter == 6:
            image_id = file[(position+1):(len(file)-4)]
            break
            
    img = Image.open(file)
    engText1 = pytesseract.image_to_string(img, lang='eng')
    textString = engText1.encode('utf-8')
    s = textString.split()
            
    for position1,name1 in enumerate(s):
        for y in range(len(nutList)):
            if name1 == nutList[y]:
                txt = "\n" + image_id + ',' + s[position1] + ',' + "english"
                dataset = dataset + txt
                print(dataset)
