import boto3
import botocore

s3 = boto3.resource('s3')

def list_all_buckets():
    #list all bucket's name
    for bucket in s3.buckets.all():
        print(bucket.name)

def upload(data_path, s3_path):
    #upload data to exist buckets
    data = open(data_path, 'rb')
    #data_path = s3_path + '/' + data_path
    s3.Bucket(s3_path).put_object(Key=data_path, Body=data,Bucket = s3_path,
                  ACL = 'public-read-write')
def create_s3_bucket(s3_path):
    #create new bucket
    s3.create_bucket(Bucket=s3_path)
def download_s3_bucket(s3_path, data, dst):
    #download file
    s3.meta.client.download_file(s3_path, data, dst)

def download_all_data(bucket_name, save_path):
    s3=boto3.client('s3')
    list=s3.list_objects(Bucket=bucket_name)['Contents']
    for s3_key in list:
        s3_object = s3_key['Key']
        if(save_path[-1] != '/'):
            save_path += '/'
        save_data_path = save_path + s3_object
        if not s3_object.endswith('/'):
            s3.download_file(bucket_name, s3_object, save_data_path)
        else:
            import os
            if not os.path.exists(s3_object):
                os.makedirs(s3_object)

# def check_exist(bucket_name):
#     exists = True
#     try:
#         s3.meta.client.head_bucket(Bucket=bucket_name)
#     except botocore.client.ClientError:
#         exists = False