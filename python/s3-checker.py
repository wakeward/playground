#!/usr/bin/env python3

import boto3, json, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a','--access-key', help='AWS Access Key ID', required=True)
parser.add_argument('-k','--secret-key', help='AWS Secret Key', required=True)
parser.add_argument('-b', '--bucket-name', help='Bucket Name', required=True)
args = parser.parse_args()

boto3.session = boto3.Session(aws_access_key_id=args.access_key, aws_secret_access_key=args.secret_key)

s3 = boto3.session.resource('s3')


def check_bucket(bucket_name):
    try:
        bucket = s3.Bucket(bucket_name)
        print(f'Bucket {bucket_name} exists')
    except Exception as e:
        print(f'Bucket {bucket_name} does not exist')

def check_public_access_block(bucket_name):
    try:
        response = s3.BucketPublicAccessBlock(bucket_name)
        print(f'Bucket {bucket_name} has public access block enabled')
    except Exception as e:
        print(f'Bucket {bucket_name} does not have public access block enabled')

def check_encryption(bucket_name):
    try:
        response = s3.BucketEncryption(bucket_name)
        print(f'Bucket {bucket_name} has encryption enabled')
    except Exception as e:
        print(f'Bucket {bucket_name} does not have encryption enabled')

def check_versioning(bucket_name):
    try:
        response = s3.BucketVersioning(bucket_name)
        print(f'Bucket {bucket_name} has versioning enabled')
    except Exception as e:
        print(f'Bucket {bucket_name} does not have versioning enabled')

def check_logging(bucket_name):
    try:
        response = s3.BucketLogging(bucket_name)
        print(f'Bucket {bucket_name} has logging enabled')
    except Exception as e:
        print(f'Bucket {bucket_name} does not have logging enabled')

def check_lifecycle(bucket_name):
    try:
        response = s3.BucketLifecycle(bucket_name)
        print(f'Bucket {bucket_name} has lifecycle enabled')
    except Exception as e:
        print(f'Bucket {bucket_name} does not have lifecycle enabled')

def check_object_lock(bucket_name):
    try:
        response = s3.BucketObjectLock(bucket_name)
        print(f'Bucket {bucket_name} has object lock enabled')
    except Exception as e:
        print(f'Bucket {bucket_name} does not have object lock enabled')

def main():
    check_bucket(args.bucket_name)
    res = check_public_access_block(args.bucket_name)
    print(res)