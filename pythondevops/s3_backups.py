"""
this is a script to take a backup from local to AWS S3
boto3 --> is a library used to do AWS tasks using python
apt install python3-boto3 -->  in case boto3 is not installed
we need to have aws account for s3 https://us-east-1.console.aws.amazon.com/s3/home?region=us-east-1#
we need to install aws cli as well: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
follow below steps:
1. go to iam section of aws
2. create a new user - "python user" (do not provide console access)
3. attach policies AmazonS3fullaccess --> create user
4. go to security credetials --> create access keys
5. select cli --> next --> create access key
6. type aws configure in the ubuntu console
7. paste the access key id: AKIA2UC3AMLHBLLTP4CA
8. paste the aws scret access key: wXj75zzjvkwfw4gwCebmprMrY65XxMBwr/d3AtEJ
9. default region and other option --> as it is
10. aws s3 ls --> to check ths list of s3 buckets in our account
"""
import boto3

s3 = boto3.resource("s3")

#in order to show all the s3 buckets
def show_buckets(s3_resource): #defining a function
    for buckets in s3_resource.buckets.all(): #iterating linewise
        print(buckets.name)

#in order to create a new s3 bucket
def create_bucket(s3_resource, bucket_name, region):
    s3_resource.create_bucket(
        Bucket = bucket_name, 
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
    print("bucket created successfully")

#in order to upload our backups on s3 bucket
def upload_backup(s3, file_name, bucket_name, key_name): #uploads a given backup file path to a given s3 bucket with a new name (key)
    data=open(file_name, 'rb') #rb is read binary
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("backup uploaded successfully")


bucket_name="pythondevopshimanshum12366"
region="us-east-2"
#create_bucket(s3, bucket_name, region)

file_name= "/home/protivitiadmin/backups/backup 2025-05-15 12:22:51.934115.tar.gz"
#upload_backup(s3,file_name, bucket_name, "my-backup.tar.gz" )

show_buckets(s3)
