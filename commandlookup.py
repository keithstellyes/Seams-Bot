import json
from functions import *
from functions.getwikipedia import getWikipedia
from functions.imdb import getIMDB
from functions.mtglookup import getMTGCard
from functions.kmathtools import listOps
from functions.kmathtools import math
from functions.etcetra import pythonEvaluator
from functions.mygooglemaps import getGMapsDirections
from functions.directMessenger import directMessage
from functions.rockpapescis import rpsGame

___name___ = "commandlookup"

def splitArgString(argstr,argcount,delimiter = " "):
    
    if len(argstr.split(" ")) > argcount:
        firstString = ""
        secondString = ""
        index = 0
        argsCounter = 0
        while argsCounter < argcount:
            firstString+=argstr[index]
            index+=1
            if argstr[index] == delimiter:
                argsCounter+=1

        args = firstString.split(delimiter)
        args.append(argstr[len(firstString)+1:])
            
        return args
    else:
        return argstr.split(" ")

def getCommand(name):
    file = open("commands.json","r")
    
    j = json.load(file)
    print(j[name])

def processEval(argstr,recipient = ""):
    ___name___ = "processEval"
    def getValidRecipients(permissionGroup):
        file = open("settings/permissions/"+permissionGroup+".txt","r")
        returnLines = file.readlines()
        file.close()
        return returnLines
    
    file = open("commands.json","r")

    j = json.load(file)
    
    identifier = argstr.split(" ")[0].lower()

    args = splitArgString(argstr,int(j[identifier]['args']))
    args[0] = args[0].lower()

    if j[args[0]].get("passrecipient") == None or j[args[0]]["passrecipient"]=="False":
        if j[args[0]]["permissions"] == "all" or recipient == "" or recipient in getValidRecipients(j[args[0]]["permissions"]):
            return eval(j[args[0]]["function"]+"(splitArgString(argstr,"+j[args[0]]["args"]+")[1:])")
        return "You are not authorized to use this command"

    #the command wants the recipient
    else:
        if not(j[args[0]]["permissions"] == "all" or recipient == "" or recipient in getValidRecipients(j[args[0]]["permissions"])):
            return "You are not authorized to use this command"
        else:
            return eval(j[args[0]]["function"]+"(splitArgString(argstr,"+j[args[0]]["args"]+")[1:]+[recipient])")
