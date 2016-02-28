import googlemaps
from datetime import *
import json
from xmlsetter import returnSetting


___name___ = "mygooglemaps"
gmaps = googlemaps.Client(key=returnSetting("googleapikey"))

#gmaps mode origin::destination

def getGMapsDirections(args):
    ___name___ = "getGMapsDirections"
    
    def directions(origin,destination,methodOfTravel):
        now = datetime.now()
        ##directions_result = gmaps.directions("Sydney Town Hall",
        ##                                     "Parramatta, NSW",
        ##                                     mode="driving",
        ##                                     departure_time=now)
        directions_result = gmaps.directions(origin,
                                             destination,
                                             mode=methodOfTravel,
                                             departure_time = now)
        returnString = ""
        for v in directions_result[0]['legs'][0]['steps']:
            returnString+="["+str(v['html_instructions'])+"]"
        returnString = returnString.replace("<b>","")
        returnString = returnString.replace("</b>","")
        returnString = returnString.replace('<div style="font-size:0.9em">',"][")
        return returnString.replace("</div>","")
    
    routeArgs = args[1].split("::")
    return directions(routeArgs[0],routeArgs[1],args[0])
    

    """
print(directions("12015 150th St Ct E, Puyallup, WA 98374",
           "City of Puyallup, 333 South Meridian, Puyallup, WA 98371",
           "driving"))
"""
