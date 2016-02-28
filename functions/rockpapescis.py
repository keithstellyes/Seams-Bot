#rockpapescis.py
__name__ = "rockpapescis"
from . import *
from sender import sendMessage
import random

def rpsGame(args):
    __name__ = "rpsGame"
    validMoves = ["rock","paper","scissors"]

    def xBeatsy(x,y):
        if x == "rock" and y == "paper":
            return False
        if x == "rock" and y == "scissors":
            return True
        if x == "paper" and y == "rock":
            return True
        if x == "paper" and y == "scissors":
            return False
        if x == "scissors" and y == "rock":
            return False
        if x == "scissors" and y == "paper":
            return True
                                               
    recipient = args[2]
    print(args,recipient)
    if args[0] != "new":
        file = open("save.txt","r")
        lines = file.readlines()
        file.close()
        mode = []
        index = 0
        while index < len(lines):
            if lines[index].startswith(args[0]+";"):
                mode = lines[index].split(";")
                break
            index+=1
        print(mode)
        game = mode[0]
        playerA = mode[1]
        playerAMove = mode[3]
        playerB = mode[2]
        playerBMove = mode[4]

        if playerA == recipient:
            playerAMove = args[1]
        elif playerB == recipient:
            playerBMove = args[1]

        if playerAMove.lower() not in validMoves or playerBMove.lower() not in validMoves:
            lines[index] = mode[0]+";"+mode[1]+";"+mode[2]+";"+playerAMove+";"+playerBMove+"\n"
            file = open("save.txt","w")
            for line in lines:
                print(line)
                file.write(line)
            file.close()
            return "Your move was "+args[1]+ ". The other player has yet to make a move"
        
        lines[index] = mode[0]+";"+mode[1]+";"+mode[2]+";x;x;\n"
        file = open("save.txt","w")
        for line in lines:
            print(line)
            file.write(line)
        file.close()
            
        if playerAMove == playerBMove:
            return "It's a tie!"        
        else:
            if xBeatsy(playerAMove.lower(),playerBMove.lower()):
                if playerA == recipient:
                    sendMessage(message= "PlayerA has won with "+playerAMove.lower(),mode = "sms",recipientOfSendMessage = playerB)
                else:
                    sendMessage(message= "PlayerA has won with "+playerAMove.lower(),mode = "sms",recipientOfSendMessage = playerA)                    
                return "PlayerA has won with "+playerAMove.lower()
            else:
                if playerA == recipient:
                    sendMessage(message= "PlayerB has won with "+playerBMove.lower(),mode = "sms",recipientOfSendMessage = playerB)
                else:
                    sendMessage(message= "PlayerB has won with "+playerBMove.lower(),mode = "sms",recipientOfSendMessage = playerA)                
                return "PlayerB has won with "+playerBMove.lower()            
    if args[0] == "new":
        gameName = str(chr(random.randrange(65,80)))+str(random.randrange(0,256))
        file = open("save.txt","r")
        lines = file.readlines()
        file.close()
        file = open("save.txt","w")
        lines.append(gameName+";"+recipient+";"+args[1]+";x;x;")
        for line in lines:
            file.write(line+"\n")
        file.close()
        sendMessage(message="You have been challenged to a game of Rock/Paper/Scissors! To make your move, type exactly, replacing rock with paper or scissors if desired: rps "+gameName+" rock",recipientOfSendMessage=args[1],mode="sms")
        return "Challenge sent. TO make your move text exactly, replacing rock with your move rps "+gameName+"rock"+args[1]
                                               
##        file = open("save.txt","w")
##        file.write(
        
        
