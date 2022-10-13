# This script gets the instance id
# Gracie 2022/10/13
import boto3

# Creating a client object that is used to interact with the AWS API.
ec2 = boto3.client("ec2")

# Calling the describe_instances method on the ec2 client object.
response = ec2.describe_instances()

# TODO: Make this work with more than one instance
# Getting the instance id from the response and printing to the console.
instance_id = response["Reservations"][0]["Instances"][0]["InstanceId"]
print(f"The Instance ID is {instance_id}")
