___name___ = "xmlsetter"

import xml.etree.ElementTree as ET

def returnSetting(settingName):
    ___name___ = "returnSetting"
    tree = ET.parse("settings/settings.xml")
    root = tree.getroot()
    return root.find(settingName).text
