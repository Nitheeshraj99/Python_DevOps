import boto3

client = boto3.client('s3') # is a common syntax  ex: boto3.client('ec2')      ex: boto3.client('ebs')

"""response = client.create_bucket(
   Bucket='niteesh-boto3',
)"""

response = client.get_bucket_acl(
    Bucket='niteesh-boto3',
)
print(response)