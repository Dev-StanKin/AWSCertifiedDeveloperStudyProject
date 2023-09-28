import boto3


def get_data():
    # get a specific record by providing the primary key
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('customerRecords')
    response = table.get_item(
        Key={
            'customerId': 'cust-71004',
            'recordCreateDate': '2023-07-20 18:26:21'
        }
    )
    print(response['Item'])
    return response['Item']


get_data()
