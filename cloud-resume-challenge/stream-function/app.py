import json
import boto3


def lambda_handler(event, context):
    
    client = boto3.client('sns')
    
    response = client.publish(
      TargetArn = "arn:aws:sns:us-east-1:684807520213:Cloud-resume",
      Message = json.dumps({'default': json.dumps("someone visited your website")}),
      MessageStructure = 'json'
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
