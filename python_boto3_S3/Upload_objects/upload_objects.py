import boto3
from botocore.exceptions import ClientError
import variables


# client = boto3.client('s3')
# upload = client.upload_file('local filepath', 'bucket name', 'destination filename')

def upload_file_to_s3():
    s3 = boto3.client('s3')
    try:
        #s3.upload_file('local filepath', 'bucket name', 's3-filepath')

        s3.upload_file(variables.local_filepath, variables.bucket_name, variables.s3_filepath)
        print("✅ Upload complete!")
        return True
    except ClientError as e:
        print("❌ Upload failed!", e)
        return False

upload_file_to_s3()