import urllib.request
import json

___name___ = "imdb"
def getIMDB(args,printReturn = False):
    ___name___ = "getIMDB"
    title = args[0]
    def returnValue(sourceList,valueName):
        indexOfValue = sourceList.index(valueName) + 1
        while l[indexOfValue] == ":":
            indexOfValue +=1
        return sourceList[indexOfValue]
    ##the below method for getting the file is now deprecated    
    #file = urllib.request.urlopen("http://www.omdbapi.com/?t="+title.replace(" ","+")+"&y=&plot=full&r=json")
    data = urllib.parse.urlencode({'t':title})
    data = data.encode('ascii')
    #print(str(data)[2:-1])
    file = urllib.request.urlopen("http://www.omdbapi.com/?"+str(data)[2:-1]+"&y=&plot=full&r=json")

                           
    json_string = file.read().decode('utf-8')
    json_obj = json.loads(json_string)

    if printReturn:
        print(json_obj["Title"] +"({}) {}".format(json_obj["Type"],json_obj["Year"]))
        print("Rated {}:".format(json_obj["Rated"]),json_obj["Plot"])
    return json_obj["Title"] +"({}) {}".format(json_obj["Type"],json_obj["Year"])+"Rated {}:".format(json_obj["Rated"])+json_obj["Plot"]
    
