from boto3.dynamodb.conditions import Key
import boto3
import json


def scan_records_for_name():
    # scans whole table looking for a specific name
    dynamodb = boto3.resource('dynamodb')
    fe = Key('name').eq('Pamela Willis')
    table = dynamodb.Table('customerRecords')
    response = table.scan(FilterExpression=fe)
    print("Scan Records for Name:")
    print("\tResult:")
    print(response)
    return response['Items']


def scan_records_for_atts():
    # https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html
    fe = Key('name').eq('Pamela Willis')
    pe = "recordCreateDate"
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('customerRecords')
    response = table.scan(
        FilterExpression=fe,
        ProjectionExpression=pe
    )
    print("Scan Records for Attributes:")
    print("\tResult:")
    print(response['Items'])
    return response['Items']


def scan_records_for_atts_reserved():
    # https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html
    fe = Key('name').eq('Pamela Willis')
    pe = "#n, recordCreateDate"
    exp_att_names = {"#n": "name"}
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('customerRecords')
    response = table.scan(
        FilterExpression=fe,
        ProjectionExpression=pe,
        ExpressionAttributeNames=exp_att_names
    )
    print("Scan Records for Attributes w reserved keywords:")
    print("\tResult:")
    print(response['Items'])
    return response['Items']


def scan_records_for_atts_reserved_sort():
    # https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html
    fe = Key('name').eq('Pamela Willis') & Key(
        'recordCreateDate').gt('2023-07-20 18:24:53')
    pe = "#n, recordCreateDate"
    exp_att_names = {"#n": "name"}
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('customerRecords')
    response = table.scan(
        FilterExpression=fe,
        ProjectionExpression=pe,
        ExpressionAttributeNames=exp_att_names
    )
    print("Scan Records for Attributes w reserved keywords Composite:")
    print("\tResult:")
    print(response['Items'])
    return response['Items']


# scan_records_for_name()
# scan_records_for_atts()
# scan_records_for_atts_reserved()
scan_records_for_atts_reserved_sort()
