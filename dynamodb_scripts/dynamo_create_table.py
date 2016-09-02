from __future__ import print_function # Python 2/3 compatibility
import boto3

boto3.set_stream_logger('botocore', level='DEBUG')
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8080")

# Logging Levels
# key value pair level | Numeric Value
table = dynamodb.create_table(
    TableName='import_logs',
    KeySchema=[
        {
            'AttributeName': 'level',
            'KeyType': 'HASH'  #Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'level',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
