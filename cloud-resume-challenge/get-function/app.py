import json
import boto3
from decimal import *

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cloud-resume-challenge')
    
    response = table.get_item(
        Key={
             'ID': 'visitors'
         }
    )
    item = response['Item']
    
    class DecimalEncoder(json.JSONEncoder):
      def default(self, obj):
        # 👇️ if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)
    
    items = json.dumps(item, cls=DecimalEncoder)
    json_object = json.loads(items)
        
    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        "body": json.dumps({'count': json_object["visitors"]}, cls=DecimalEncoder),
    }
