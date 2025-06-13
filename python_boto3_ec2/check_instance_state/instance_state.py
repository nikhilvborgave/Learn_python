import boto3
import pandas as pd

client = boto3.client('ec2', region_name='us-east-1')

def describe_instance():
    response = client.describe_instance_status(
        InstanceIds=[],
        DryRun= False,      #checks if you have valid permissions
        IncludeAllInstances=True
    )

    for instance in response.get("InstanceStatuses", []):
        instance_id = instance.get("InstanceId", "N/A")
        state = instance.get("InstanceState", {}).get("Name", "Unknown")
        ec2_id = instance_id
        Instance_status = state
        return ec2_id, Instance_status     #returns values of instance id & status


table = []
describe_ec2 = client.describe_instances(
    InstanceIds=[],
    DryRun= False,      #checks if you have valid permissions
)

for reservation in describe_ec2.get("Reservations", []):
    for instance in reservation.get("Instances", []):
         # Extract Name tag if available
        name = None
        for tag in instance.get("Tags", []):
            if tag["Key"] == "Name":
                name = tag["Value"]
        instance_public_ip = instance.get("PublicIpAddress", "N/A")
        instance_private_ip = instance.get("PrivateIpAddress", "N/A")
        #calls describe_instance function and stores values resp.
        ec2_id, Instance_status = describe_instance()  
        table.append({
            "Instance Id ": instance.get("InstanceId"),
            "Instance Name": name,
            "Public Ip": instance_public_ip,
            "Private Ip": instance_private_ip,
            "Status": Instance_status,
        })

# Create DataFrame
df = pd.DataFrame(table)

# Save to CSV
df.to_csv("instance_state.csv", index=False)
print("Complete!!")