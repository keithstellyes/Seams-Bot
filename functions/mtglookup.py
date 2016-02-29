import json

___name___ = "mtg"

def getMTGCard(args):
    ___name___ = "getMTGCard"

    def addValueIfHas(j,key,string="",rString = "|",elseString=""):
        returnString = ""
        
        if j[name].get(key):
            returnString = string+j[name][key]+rString
        else:
            returnString = elseString
        return returnString
    
    name = args[0]
    file = open("AllCards.json","r")
    
    j = json.load(file)
    file.close()
    cardText = ""
    returnString = name+"|"

    returnString+=addValueIfHas(j,"manaCost")
    returnString += addValueIfHas(j,"type")
    returnString+= addValueIfHas(j,key="text",elseString="Text: Vanilla",string="Text:")
    ptString = ""
    ptString+= addValueIfHas(j,key="power",string="P/T:",rString = "")
    ptString+=addValueIfHas(j,key="toughness",string="/")
    returnString+=ptString

    return returnString.replace("â€”","-")
print(getMTGCard(["Counterspell"]))
print(getMTGCard(["Forest"]))
print(getMTGCard(["Izzet Staticaster"]))
