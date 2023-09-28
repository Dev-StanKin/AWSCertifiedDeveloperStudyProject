import boto3
from datetime import datetime


def create_record():
    client = boto3.client('dynamodb')
    try:
        client.put_item(
            TableName='customerRecords',
            Item={
                'customerId': {'S': 'cust-71004'},
                'recordCreateDate': {'S': f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'},
                'name': {'S': 'Pamela Willis'},
                'address': {'S': '123 Main St.'},
                'age':{'N': '35'}
            }
        )
    except Exception as e:
        print(e)
        raise e
    return {'statusCode': 200}


create_record()
