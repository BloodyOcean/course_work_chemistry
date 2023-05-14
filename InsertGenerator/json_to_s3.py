import boto3
import os

# Set your AWS credentials
aws_access_key_id = ''
aws_secret_access_key = ''


def upload_directory_to_s3(local_directory, bucket_name, s3_prefix=''):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)


    for root, dirs, files in os.walk(local_directory):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, local_directory)
            s3_path = os.path.join(s3_prefix, relative_path).replace("\\", "/")

            s3.upload_file(local_path, bucket_name, s3_path)
            print(f'Uploaded {local_path} to s3://{bucket_name}/{s3_path}')


# Set the bucket name and file details
bucket_name = 'pharmacy-objects'
dir_path = "./InsertGenerator/GeneratedJson"
s3_folder_key = ""

upload_directory_to_s3(dir_path, bucket_name)
