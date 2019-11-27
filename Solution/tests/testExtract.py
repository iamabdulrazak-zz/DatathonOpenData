def readFile():
    #this function to read the file  and check if its readable then print it
    file = open("in.txt", "r")
    if file.mode =='r':
        content = file.readlines()
        print(content)

def wordExtract():
    #this function to read the file  and  print specific word
    nutList = ["energy","total fat","saturated fat", "monounsaturated fat", "polysaturated fat","trans fat",
    "cholestrol","sodium", "total carbohydrate", "dietary fiber", "sugar", "protein", "vitamin c", "calcium",
    "iron", "calories", "total sugars", "potassium", "fat", "saturated", "trans", "carbohydrate",  "sugars",
    "added sugars", "added sugar", "vitamin a", "vitamin d", "salt"]
    with open("out.txt") as file:
        for line in file:
            s = line.split()
            for i,j in enumerate(s):
                for y in range(len(nutList)):
                    if j == nutList[y]:
                        print(s[i])
readFile()
wordExtract()