import json
#from commands import *
from commands.getwikipedia import getWikipedia
from commands.imdb import getIMDB
from commands.mtglookup import getMTGCard
from commands.kmathtools import listOps
from commands.kmathtools import math
from commands.etcetra import pythonEvaluator
from commands.mygooglemaps import getGMapsDirections
from commands.directMessenger import directMessage
from commands.rockpapescis import rpsGame

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

def processEval(argstr,recipient = "",breakstring = "|"):
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

    funcString = j[args[0]]["function"]
    funcSplitArgString = "(splitArgString(argstr,"+j[args[0]]["args"]+")[1:]"
    recipientSetString = ""
    breakSetString = ""
    #check if command wants the recipient variable

    if not(j[args[0]].get("passrecipient") == None or j[args[0]]["passrecipient"]=="False"):
        recipientSetString = ", recipient='"+recipient+"'"

    if not(j[args[0]].get("breakstring") == None or j[args[0]]["breakstring"]=="False"):
        breakSetString = ", breakString=breakstring"
    
    if j[args[0]]["permissions"] == "all" or recipient == "" or recipient in getValidRecipients(j[args[0]]["permissions"]):
        return eval(funcString+funcSplitArgString+recipientSetString+breakSetString+")")
    return "You are not authorized to use this command"

    #the command wants the recipient
##    else:
##        if not(j[args[0]]["permissions"] == "all" or recipient == "" or recipient in getValidRecipients(j[args[0]]["permissions"])):
##            return "You are not authorized to use this command"
##        else:
##            return eval(funcString+funcSplitArgString+"+[recipient])")
