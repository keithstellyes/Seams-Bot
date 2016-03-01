import os, sys
import json

___name___ = "mtg"

def getMTGCard(args,breakString = "|"):
    ___name___ = "getMTGCard"

    def addValueIfHas(j,key,string="",rString = breakString,elseString=""):
        returnString = ""
        
        if j[name].get(key):
            returnString = string+j[name][key]+rString
        else:
            returnString = elseString
        return returnString
    
    name = args[0]
    file = open(os.path.dirname(sys.argv[0])+"/AllCards.json","r")
    
    j = json.load(file)
    file.close()
    cardText = ""
    if j.get(name) == None:
        #Check for capitalization
        name = name.title()
        if j.get(name) == None:
            #another common issue
            name = name.replace(" ","-")
            if j.get(name) == None:
                return name+" not found."
            
    returnString = name+breakString
    returnString+=addValueIfHas(j,"manaCost")
    returnString += addValueIfHas(j,"type")
    returnString+= addValueIfHas(j,key="text",elseString="Text: Vanilla"+breakString,string="Text:")
    ptString = ""
    ptString+= addValueIfHas(j,key="power",string="P/T:",rString = "")
    ptString+=addValueIfHas(j,key="toughness",string="/")
    returnString+=ptString

    return returnString.replace("â€”","-")
