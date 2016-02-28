#directMessenger.py

from . import *
from sender import sendMessage
from profiler import getProfile

__name__ = "directMessenger"

def directMessage(args):
    __name__ = "directMessage"
    if args[0] == "sms-p":
        args[0] = "sms"
        args[1] = getProfile(args[1],"phonenumber")
    sendMessage(mode = args[0],recipientOfSendMessage=args[1],message = args[2])
