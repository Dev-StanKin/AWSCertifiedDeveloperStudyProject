import boto3


def update():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('customerRecords')
    response = table.update_item(
        Key={
            'customerId': 'cust-592869',
            'recordCreateDate': '2023-07-20 18:15:27'
        },
        UpdateExpression='SET age = :val1',
        ExpressionAttributeValues={
            ':val1': 25
        },
        ReturnValues='UPDATED_NEW'
    )
    print(response)


def batch_delete():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('customerRecords')
    with table.batch_writer() as batch:
        batch.delete_item(
            Key={
                'customerId': 'cust-71004',
                'recordCreateDate': '2023-07-20 18:15:33'
            }
        )
        batch.delete_item(
            Key={
                'customerId': 'cust-71004',
                'recordCreateDate': '2023-07-20 18:23:49'
            }
        )


batch_delete()
