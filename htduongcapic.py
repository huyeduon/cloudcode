import boto3
import requests
import sys
from botocore.config import Config
# current boto3 version is 1.15.8
# config for sydney region
htduong_config = Config(
    region_name = 'ap-southeast-2',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

ec2 = boto3.client('ec2', config=htduong_config)
response = ec2.describe_instances()
print(response)
