from commandlookup import processEval

inputStr = ""
while True:
    inputStr = input("Input:")
    if not(inputStr.lower().startswith("quit") or inputStr.lower().startswith("exit")):
        print(processEval(inputStr))
    else:
        break
