properties={};
properties["general"] = ["General", "ABC", 100]

def getPropertiesDB():
    return properties


def addProperties(propertyName, propertyPrefix):
    properties[propertyName] = [propertyName, propertyPrefix, 0];


def generateTicket(propertyName):
    if (properties[propertyName]):
        properties[propertyName][2] = properties[propertyName][2]+1
        return properties[propertyName]
    return -1
    
def getLastTicket(propertyName):
    if (properties[propertyName]):
        return properties[propertyName][2]
    return -1
    
