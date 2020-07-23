import json
from departments import generateTicket, getPropertiesDB
def lambda_handler(event, context):
    property = getPropertiesDB()
    userDeptRequest = event['queryStringParameters']['deptName']
    
    resJson = {}
    if (property[userDeptRequest]):
        result = generateTicket(userDeptRequest)
        resJson['Name'] = result[0]
        resJson['UsecaseID'] = result[1] + str(result[2])

    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(resJson)
    return responseObject
