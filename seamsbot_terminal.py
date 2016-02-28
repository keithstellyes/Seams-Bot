from commandlookup import processEval

inputStr = ""
while not (inputStr.lower().startswith("quit") or inputStr.lower().startswith("exit")):    
    inputStr = input("Input:")
    print(processEval(inputStr))
