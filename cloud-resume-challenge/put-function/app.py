import json
import boto3


def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cloud-resume-challenge')
     
    table.update_item(
         Key={
             'ID': 'visitors'
         },
         UpdateExpression= 'ADD visitors :inc',
         ExpressionAttributeValues={
             ':inc': 1
         }
     )
             
             
    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        "body": json.dumps(
            {
                
            }
        ),
    }
