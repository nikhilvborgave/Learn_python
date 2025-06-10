import boto3

client = boto3.client('s3')

new_bucket = "254466556549-test-bucket-from-pythonboto3"
response = client.create_bucket(
    Bucket= new_bucket,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1',
    }
)

encryption_response = client.put_bucket_encryption(
    Bucket = new_bucket,
    ServerSideEncryptionConfiguration={
    'Rules': [
            {
                'ApplyServerSideEncryptionByDefault': {
                    'SSEAlgorithm': 'AES256',
                },
                'BucketKeyEnabled': True
            },
        ]
    },
)

versioning_response = client.put_bucket_versioning(
    Bucket= new_bucket,
    VersioningConfiguration={
        'Status': 'Enabled',
    },
)