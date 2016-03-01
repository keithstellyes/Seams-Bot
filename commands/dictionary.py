from xmlsetter import returnSetting

__name__ = "dictionary"

def loadSettings():
    preferredcollegiate = returnSetting("preferredcollegiate")
    preferredspen = returnSetting("preferredsp-en")

    collegiatekey = ""
    spenkey = ""

    if preferredcollegiate == "merriam":
        collegiatekey = returnSetting("merriamcollegiatekey")
    if preferredspen == "merriam":
        spenkey = returnSetting("merriamsp-enkey")
    return [preferredcollegiate,collegiatekey,preferredspen,spenkey]

def lookupWord(args):
    def collegiateLookup(word,preferred,api):
        return word+"lookedup"
    def spenLookup(word):
        return word+"lookedup"
        
    if args[0] == "en":
        return collegiateLookup(args[1])
        

