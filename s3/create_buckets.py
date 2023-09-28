import boto3

s3 = boto3.resource('s3')

# create a new bucket if it doesn't exist already


def create_bucket(bucket_name, region='us-east-2'):
    if s3.Bucket(bucket_name) not in s3.buckets.all():
        location = {'LocationConstraint': region}
        s3.create_bucket(Bucket=bucket_name,
                         CreateBucketConfiguration=location)
        print("Bucket created: " + bucket_name)
    else:
        print("Bucket already exists: " + bucket_name)

# Create a new public that is readable by everyone
# To create this Public bucket,which is not recommeded by AWS as it posess as a Security risk, use the client method ie;
# s3 = boto3.client('s3')


def create_public_bucket(bucket_name, region='us-east-2'):
    if bucket_name not in [bucket['Name'] for bucket in s3.list_buckets()['Buckets']]:
        location = {'LocationConstraint': region}
        s3.create_bucket(Bucket=bucket_name,
                         CreateBucketConfiguration=location, ObjectOwnership='ObjectWriter')
        s3.put_public_access_block(Bucket=bucket_name, PublicAccessBlockConfiguration={
                                   'BlockPublicAcls': False, 'IgnorePublicAcls': False, 'BlockPublicPolicy': False, 'RestrictPublicBuckets': False})
        s3.put_bucket_acl(ACL='public-read-write', Bucket=bucket_name)
        print("Public bucket created: " + bucket_name)
    else:
        print("Bucket already exists: " + bucket_name)

# Create a new private bucket that is readable by the owner only


def create_private_bucket(bucket_name, region='us-east-2'):
    if s3.Bucket(bucket_name) not in s3.buckets.all():
        location = {'LocationConstraint': region}
        s3.create_bucket(Bucket=bucket_name, ACL='private',
                         CreateBucketConfiguration=location)
        print("Private bucket created: " + bucket_name)
    else:
        print("Bucket already exists: " + bucket_name)


# create_bucket('stan-def-bucket')
# create_public_bucket('stan-public-bucket')
# create_private_bucket('stan-private-bucket')

# Retrieve the list of existing buckets
s3c = boto3.client('s3')
response = s3c.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
