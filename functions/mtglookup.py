import json

___name___ = "mtg"

def getMTGCard(args):
    ___name___ = "getMTGCard"
    name = args[0]
    file = open("AllCards.json","r")
    
    j = json.load(file)
    cardText = ""
    
    if j[name].get('text') == None:
        cardText = "Vanilla"
    else:
        cardText = j[name]["text"]
    
    return "Mana cost:"+j[name]["manaCost"]+"Color Identity"+str(j[name]["colorIdentity"])+"Type:"+j[name]["type"]+"Card text:"+cardText+"P/T:"+j[name]["power"]+"/"+j[name]["toughness"]
