import boto3

client = boto3.client('ec2', region_name='us-east-1')

response = client.describe_instance_status(
    InstanceIds=[],
    DryRun= False,      #checks if you have valid permissions
    IncludeAllInstances=True
)

for instance in response.get("InstanceStatuses", []):
    instance_id = instance["InstanceId"]
    state = instance["InstanceState"]["Name"]
    print(f"instance_id = {instance_id}")
    print(f"status = {state}")


# print("Instance details: ")
# print(f"- {response} ")        #prints bucket name with date of creation
