# A Number/Reference Generation Rest API, to be used with Amazon Web Service's API Gateway application.

## Application Features:
Generates a number with prefix. i.e. ABC123 and increments the number whenever the GET request is sent to the API.
Use AWS API Gateway as the Gateway handler/handler.

Expected Get Query Params = "deptName"=general
https://xxxxxxx.execute-api.us-east-1.amazonaws.com/devstageprod/resource?deptName=general

## Typical Usage:
- Ticketing system
- HelpDesk
- Shopping Cart ...

## Technology:
* AWS Lambda
* AWS API Gatewat
* Python

## Expected Output
Screenshot:
![JSON output screenshot](https://github.com/tomiwaog/NumberGeneratorAPILambda/blob/master/screenshot.PNG?raw=true)
