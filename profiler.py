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

def getProfileParse(string):
    __name__ = "getProfileParse"
    string = string[1:-1]
    args = string.split("::")
    
    file = open("settings/profiles.json","r")
    j = json.load(file)
    file.close()
    return j[args[1]][args[2]]

def getProfile(name,key):
    __name__ = "getProfile"
    
    file = open("settings/profiles.json","r")
    j = json.load(file)
    file.close()
    return j[name][key]    
