import boto3
import json


def get_data():
    # check consumed capacity when swapping consistent read for eventual
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('customerRecords')
    response = table.get_item(
        Key={
            'customerId': 'cust-71004',
            'recordCreateDate': '2023-07-20 18:26:21'
        },
        ReturnConsumedCapacity='TOTAL',
        ConsistentRead=True
    )
    print(json.dumps(response, indent=2))
    return response['Item']


get_data()
