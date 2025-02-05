#!/usr/bin/env python3

import boto3, json, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a','--access-key', help='AWS Access Key ID', required=True)
parser.add_argument('-k','--secret-key', help='AWS Secret Key', required=True)
parser.add_argument('-b', '--bucket-name', help='Bucket Name', required=True)
args = parser.parse_args()

s3r = boto3.resource('s3',aws_access_key_id=args.access_key, aws_secret_access_key=args.secret_key)
s3 = boto3.client('s3',aws_access_key_id=args.access_key, aws_secret_access_key=args.secret_key)

def check_bucket(bucket_name):
    s3r.Bucket(bucket_name)
    if not s3r.Bucket(bucket_name) in s3r.buckets.all():
        print(f'Bucket {bucket_name} does not exist')
        exit(1)
    return {"BucketName": bucket_name}

def check_public_access_block(bucket_name):
    try:
        response = s3.get_public_access_block(Bucket=bucket_name)
        data = json.dumps(response)
        lj = json.loads(data)
        del lj['ResponseMetadata']
        return lj
    except Exception:
        return {"PublicAccessBlockConfiguration": "Not Configured"}

def check_encryption(bucket_name):
    try:
        response = s3.get_bucket_encryption(Bucket=bucket_name)
        data = json.dumps(response)
        lj = json.loads(data)
        del lj['ResponseMetadata']
        return lj
    except Exception:
        return {"ServerSideEncryptionConfiguration": "Not Configured"}

def check_versioning(bucket_name):
    try:
        response = s3.get_bucket_versioning(Bucket=bucket_name)
        data = json.dumps(response)
        lj = json.loads(data)
        del lj['ResponseMetadata']
        return lj
    except Exception:
        return {"BucketVersioning": "Not Configured"}

def check_logging(bucket_name):
    try:
        response = s3.get_bucket_logging(Bucket=bucket_name)
        data = json.dumps(response)
        lj = json.loads(data)
        del lj['ResponseMetadata']
        return lj
    except Exception:
        return {"BucketLogging": "Not Configured"}

def check_lifecycle(bucket_name):
    try:
        response = s3.get_bucket_lifecycle(Bucket=bucket_name)
        data = json.dumps(response)
        lj = json.loads(data)
        del lj['ResponseMetadata']
        return lj
    except Exception:
        return {"BucketLifeCycleConfiguration": "Not Configured"}

def check_object_lock(bucket_name):
    try:
        response = s3.get_object_lock_configuration(Bucket=bucket_name)
        data = json.dumps(response)
        lj = json.loads(data)
        del lj['ResponseMetadata']
        return lj
    except Exception:
        return {"ObjectLockConfiguration": "Not Configured"}

def merge_json(json1, json2):
    return {**json1, **json2}

buck = check_bucket(args.bucket_name)
pab = check_public_access_block(args.bucket_name)
init0 = merge_json(buck, pab)
enc = check_encryption(args.bucket_name)
init1 = merge_json(init0, enc)
ver = check_versioning(args.bucket_name)
init2 = merge_json(init1, ver)
log = check_logging(args.bucket_name)
init3 = merge_json(init2, log)
lif = check_lifecycle(args.bucket_name)
init4 = merge_json(init3, lif)
ol = check_object_lock(args.bucket_name)
init5 = merge_json(init4, ol)

print(json.dumps(init5, indent=4, sort_keys=True))
