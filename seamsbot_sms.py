import time
import datetime
from bs4 import BeautifulSoup
import urllib.request
from twilio.rest import TwilioRestClient
import statistics
from commandlookup import processEval
from xmlsetter import returnSetting

___name___ = "seamsbot"

"""
Fr
"""
###TWILIO
account_sid = returnSetting("twilio_account_sid")
auth_token = returnSetting("twilio_auth_token")
client = TwilioRestClient(account_sid, auth_token)
###

serverNumber = returnSetting("servercontact")

recipient = ""

def send(string):
    print(string)
    print("Sent to:"+str(recipient))
    message = client.messages.create(to=str(recipient),
                                     from_=serverNumber,
                                     body=string)
def process(argstr):
    send(processEval(argstr,recipient))

def poll(pollDelay):
    messagesLast = []
    for message in client.messages.list():
        messagesLast.append(message.body)

        
    #Checks to see if there's a difference in lists, if so, return the
    #discrepancy
    def listDifference(list1,list2):
        returnlist = []
        if len(list1) != len(list2):
            index = 0
            index = len(list1)
            while index < len(list2):
                returnlist.append(list2[index])
                index+=1
        return returnlist
    
    while True:
        global recipient
        messages = []
        for message in client.messages.list(to=serverNumber):
            messages.append(message.body)
        recipient = client.messages.list()[1].from_
        
        #This means that we've gotten new messages!
        if messagesLast[1] != messages[1] and recipient!=serverNumber:
            print("!")
            print(messages[0])
            process(messages[0])
            messagesLast = messages[:]
        else:
            print("_",end="")
        time.sleep(pollDelay)
while True:
    try:
        poll(5)
    except Exception as e:
        print("Sent to:"+str(recipient))
        message = client.messages.create(to=returnSetting("admincontact"),
                                          from_=serverNumber,
                                     body="ERROR:"+str(e))
        time.sleep(120)

