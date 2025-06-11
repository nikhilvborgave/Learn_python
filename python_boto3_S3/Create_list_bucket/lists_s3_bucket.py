import boto3

client = boto3.client('s3')

response = client.list_buckets()

print("S3 Buckets:")
for bucket in response['Buckets']:
    print(f"- {bucket['Name']} (Created: {bucket['CreationDate']})")        #prints bucket name with date of creation

    #checking if versioning is enabled
    versioning_response = client.get_bucket_versioning(Bucket=bucket['Name'])
    status = versioning_response.get('Status')
    if status is None:
        print("  Versioning: Not Enabled")
    else:
        print(f"  Versioning: {status}")
    

# response = client.get_bucket_versioning(Bucket='254466556549-test-bucket')
# status = response.get('Status')
# print({status})