from boto3.dynamodb.conditions import Key
import boto3
import json


def query_records_for_custId():
    # must provide a partition key
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.query(
        TableName='customerRecords',
        KeyConditionExpression='customerId = :customerId',
        ExpressionAttributeValues={
            ':customerId': {'S': 'cust-71004'}
        },
        ReturnConsumedCapacity='TOTAL'
    )
    print("Query Records for Name:")
    print("\tResult:")
    print(response)
    return response['Items']


def query_records_for_custId_sort():
    # must provide a partition key
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.query(
        TableName='customerRecords',
        KeyConditionExpression='customerId = :customerId AND recordCreateDate = :recordCreateDate',
        ExpressionAttributeValues={
            ':customerId': {'S': 'cust-71004'},
            ':recordCreateDate': {'S': '2023-07-20 18:26:21'}
        }
    )
    print("Query Records for Name with sort key:")
    print("\tResult:")
    print(response)
    return response['Items']


def query_records_for_custId_sortOps():
    # must provide a partition key
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.query(
        TableName='customerRecords',
        KeyConditionExpression='customerId = :customerId AND recordCreateDate > :recordCreateDate',
        ExpressionAttributeValues={
            ':customerId': {'S': 'cust-71004'},
            ':recordCreateDate': {'S': '2023-07-20 18:23:49'}
        }
    )
    print("Query Records for Name with sort key Ops:")
    print("\tResult:")
    print(response['Items'])
    return response['Items']


def query_records_for_custId_sortOps_pe():
    # must provide a partition key
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.query(
        TableName='customerRecords',
        KeyConditionExpression='customerId = :customerId AND recordCreateDate > :recordCreateDate',
        ExpressionAttributeValues={
            ':customerId': {'S': 'cust-71004'},
            ':recordCreateDate': {'S': '2023-07-20 18:23:49'}
        },
        ProjectionExpression='customerId, recordCreateDate',
        ReturnConsumedCapacity='TOTAL'
    )
    print("Query Records for Name with sort key Ops PE:")
    print("\tResult:")
    print(response)
    return response['Items']


# query_records_for_custId()
# query_records_for_custId_sort()
# query_records_for_custId_sortOps()
query_records_for_custId_sortOps_pe()
