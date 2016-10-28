from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

def create_error(error):

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('import_logs')

    level = 50
    date = '01/11'
    error_message = error

    table.put_item(
       Item={
            'level': level,
            'error': {
                'date': date,
                'error_message': error_message
            }
        }
    )
    print(error_message)
    print("PutItem succeeded:")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))
