#sender.py

#used by commands that send to messages more than just the default

from twilio.rest import TwilioRestClient
from xmlsetter import returnSetting

___name___ = "sender"
###TWILIO
account_sid = returnSetting("twilio_account_sid")
auth_token = returnSetting("twilio_auth_token")
client = TwilioRestClient(account_sid, auth_token)
###

serverNumber = returnSetting("servercontact")

def sendMessage(message,mode = "print",recipientOfSendMessage = "default"):
    ___name___ = "sendMessage"
    if recipientOfSendMessage == "default":
        print("Warning: sendMessage recipient left on default")
    if mode == "print":
        print(message)
    elif mode == "sms" and recipientOfSendMessage != "default":
        print(message)
        print("Sent to:"+str(recipientOfSendMessage))
        message = client.messages.create(to=str(recipientOfSendMessage),
                                         from_=serverNumber,
                                         body=message)
    elif mode == "sms" and recipientOfSendMessage == "default":
         raise Exception("recipientOfSendMessage() not set.")
    elif mode != "sms" and mode!="print":
        raise Exception("No valid mode for sendMessage() set!")
