import boto3
import json

print('Loading function')
dynamo = boto3.client('dynamodb')
TableName = 'hitcount'


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''
    #print("Received event: " + json.dumps(event, indent=2))
    
    getCount = dynamo.get_item(
        TableName='hitcount',
        Key = {
            'hitcounterpartkey': {'S': 'key0'}
        }
    )
    
    prevViewCount = getCount['Item']['hitcount']['N']
    
    updateCount = dynamo.update_item(
        TableName='hitcount',
        Key = {
            'hitcounterpartkey': {'S': 'key0'}
        },
        UpdateExpression = 'ADD hitcount :inc',
        ExpressionAttributeValues = {":inc" : {"N": "1"}},
        ReturnValues = 'UPDATED_NEW'
        )
    
    value = updateCount['Attributes']['hitcount']['N']
    
    return {      
            'statusCode': 200,

            'body': getCount}