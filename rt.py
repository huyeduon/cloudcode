import boto3
import sys
from botocore.config import Config
import json
# current boto3 version is 1.15.8
# config for sydney region
# this code will update route infra vpc routable

htduong_config = Config(
    region_name = 'ap-southeast-2',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

ec2 = boto3.resource('ec2', config=htduong_config)
client = boto3.client('ec2', config=htduong_config)

filters = [{'Name':'tag:Name', 'Values':['context-[overlay-1]*']}]

vpcs = list(ec2.vpcs.filter(Filters=filters))

for vpc in vpcs:
    response = client.describe_vpcs(
        VpcIds=[
            vpc.id,
        ]
    )
    print("Infra VPC Cidr block:", response["Vpcs"][0]["CidrBlock"])
    print("Infra VPC Id:", response["Vpcs"][0]["VpcId"])

#    print(json.dumps(response, sort_keys=True, indent=4))


