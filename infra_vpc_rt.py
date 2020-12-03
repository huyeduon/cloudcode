import boto3
import sys
from botocore.config import Config
# current boto3 version is 1.15.8
# config for sydney region
# this code will update route infra vpc routable

# eni-0f4033ca2163e7b7e is csr-0 gi2
# eni-02d386ad5afc8148e is csr-1 gi2
# rtb-03d9beedfb8be6365: 10.11.0.176/24
# rtb-0141da8998d707974: 10.11.0.240/24

htduong_config = Config(
    region_name = 'ap-southeast-2',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

ec2 = boto3.resource('ec2', config=htduong_config)

csr_0_rt = ec2.RouteTable('rtb-03d9beedfb8be6365')
csr_0_gi2 = 'eni-0f4033ca2163e7b7e'

csr_1_rt = ec2.RouteTable('rtb-0141da8998d707974')
csr_1_gi2 = 'eni-02d386ad5afc8148e'

# delete default route on rt-0
client = boto3.client('ec2', config=htduong_config)
response = client.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId='rtb-03d9beedfb8be6365'
)

# update route table infra_vpc rt subnet of TGW
default_route_csr_1 = csr_0_rt.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    NetworkInterfaceId=csr_0_gi2
)

# delete default route on rt-1
client = boto3.client('ec2', config=htduong_config)
response = client.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId='rtb-0141da8998d707974'
)

# update route table infra_vpc rt subnet of TGW
default_route_csr_1 = csr_1_rt.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    NetworkInterfaceId=csr_0_gi2
)
