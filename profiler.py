#profiler.py
#turns the following string
#[P::name::data]
#to grab from the profiles.json the key to name
#for example,
#[P::name::phonenumber]
#returns
#the phone number of the name of that profile
import json
__name__ = "profiler"

def getJSON():
    file = open("settings/profiles.json","r")
    j = json.load(file)
    file.close()
    return j

def getProfileParse(string):
    __name__ = "getProfileParse"
    string = string[1:-1]
    args = string.split("::")
    j = getJSON()
    if "::" not in string:
        return string
    return j[args[1]][args[2]]
def getProfile(name,key):
    __name__ = "getProfile"
    j = getJSON()
    
    return j[name][key]

#finds the first profile name searching by desired key and value
def findProfileNameByKeyValue(key,value):
    __name__ = "findProfileNameByKeyValue"
    j = getJSON()
    names = []
    for name in j:
        names.append(name)   
    for name in names:
        if j[name][key] == value:
            return name
    return None
#returns a list of all profile names with the corresponding value

def findAllProfileNameByKeyValue(key,value):
    __name__ = "findAllProfileNameByKeyValue"
    j = getJSON()
    names = []
    returnNames = []
    for name in j:
        names.append(name)
        
    for name in names:
        if j[name][key] == value:
            returnNames.append(name)
    return returnNames    

#ID refers to an identifier for that piece of data
#might be a command name, a game name, etc. returns None if not in it
#With every ID there is a corresponding string
#supports searching by name or phone number and in the future by email
#name is checked first, then phone number
#If multiple share the same data point, it will perform undesirably, but can
#be assumed it won't happen
def profileGetData(ID,name = "",phonenumber="",email=""):
    __name__ = "profileGetData"
    def getData(name,ID):
        workingList = getProfile(name,"data")
        for dataTuplet in workingList:
            if dataTuplet[0] == ID:
                return dataTuplet[1]
        return None
    
    if name == "" and phonenumber == "" and email == "":
        Exception("No valid profile identifiers for profileGetData")
        
    elif name != "":
        return getData(name,ID)
    elif phonenumber!= "":
        return getData(findProfileNameByKeyValue("phonenumber",phonenumber),ID)
    
def profileWriteData(ID,name = "",phonenumber="",email="",newData = ""):
    __name__ = "profileWriteData"
    
    if "}," or "'" in newData:
        return Exception("The }, sequence and the ' character are not currently supported for data writing")
                  
    if phonenumber!= "":
        name = findProfileNameByKeyValue("phonenumber",phonenumber)
    j = getJSON()
    dataTuplets = j[name]['data']
    index = 0
    while index < len(j[name]['data']):
        if j[name]['data'][index][0] == ID:
            j[name]['data'][index][1] = newData
        index+=1
    def processIt(string):
        lastChar = ""
        myString = ""
        for char in string:
            myString+=char
            if lastChar+char == "},":
                myString+="\n"
            lastChar = char
        return ("{\n"+myString[1:-1]+"\n}").replace("'",'"')
    outfile = open("output.json","w")
    outfile.write(processIt(str(j)))
    outfile.close()
