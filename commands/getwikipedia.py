import wikipedia
___name___ = "getwikipedia"


def getWikipedia(args):
    __name__ = "getWikipedia"
    #syntax:
    #wikipedia random
    #wikipedia article
    try:
        if args[0].lower() == "article":
            return wikipedia.summary(args[1],sentences=2)
        
    except wikipedia.exceptions.DisambiguationError as e:
        return str(e)
        
    if args[0].lower() == "random":
        desiredArticleSummary = ""
        while len(desiredArticleSummary) <150:
            try:
                desiredArticleSummary = wikipedia.summary(wikipedia.random())
            except wikipedia.exceptions.DisambiguationError as e:
                print("Tried; disambiguation hitch; trying again")
        return desiredArticleSummary
