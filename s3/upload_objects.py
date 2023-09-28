import boto3
# Create an S3 client
s3 = boto3.client('s3')


def upload_files(filename=None, bucket=None, object_name=None):
    if filename is None:
        filename = 'upload.txt'
    if bucket is None:
        bucket = 'stan-def-bucket'
    if object_name is None:
        object_name = 'upload.txt'
    s3.upload_file(filename, bucket, object_name)
    print(f"Uploaded {filename} to {bucket} as {object_name}")


def upload_files_pub(filename=None, bucket=None, object_name=None):
    if filename is None:
        filename = 'upload.txt'
    if bucket is None:
        bucket = 'stan-def-bucket'
    s3.upload_file(filename, bucket, object_name,
                   ExtraArgs={
                       'GrantRead': 'uri="http://acs.amazonaws.com/groups/global/AllUsers"'})
    print(f"Uploaded {filename} to {bucket} as {object_name}")

# List all objects in a bucket


def list_objects(bucket=None):
    if bucket is None:
        bucket = 'stan-def-bucket'
    response = s3.list_objects(Bucket=bucket)
    for content in response.get('Contents', []):
        print(content.get('Key'))


def upload_if_not_exists(filename=None, bucket=None, object_name=None):
    if filename is None:
        filename = 'upload.txt'
    if bucket is None:
        bucket = 'stan-def-bucket'
    response = s3.list_objects(Bucket=bucket)
    record = [k for k in response.get('Contents')
              if k.get('Key') == object_name]
    if len(record) < 1:
        s3.upload_file(filename, bucket, object_name)
        print(
            f"Uploaded {filename} to {bucket} with object name {object_name}")
    else:
        print(f"File {object_name} already exists in {bucket}")


upload_files('upload.txt', 'stan-def-bucket', 'upload.txt')
upload_files('upload.txt', 'stan-def-bucket', 'oops.txt')
upload_files_pub('upload.txt',
                 'stan-def-bucket', 'pub.txt')
list_objects()

upload_if_not_exists('upload.txt', 'stan-def-bucket', 'upload.txt')
