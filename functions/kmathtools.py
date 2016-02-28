import statistics

___name___ = "kmathtools"

def listOps(args):
    ___name___ = "listOps"
    myList = args[0]
    myNumbers = []
    for n in myList.split(","):
        myNumbers.append(int(n))
    return "List Size="+str(len(myNumbers))+",Mean="+str(float(sum(myNumbers))/len(myNumbers))+",Median="+str(statistics.median(myNumbers))+",Mode="+str(max(set([5,5,3]), key=[5,5,3].count))
        
def math(args):
    ___name___ = "math"
    def scrubber(string):
        isClean = True
        for character in string:
            if character.isalpha():
                isClean = False
        return isClean
    isClean = scrubber(args[0])
    if not isClean:
        return "ERROR BAD INPUT"
    
    return eval(args[0].replace("^","**"))

