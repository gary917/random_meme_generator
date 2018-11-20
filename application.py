from flask import Flask, render_template, request
import os
import config
import boto3
import random

HOST_NAME = 's3-ap-southeast-2.amazonaws.com/'
BUCKET_NAME = 'meme-generator-source'  # replace with your bucket name
URI = 'https://' + HOST_NAME + BUCKET_NAME

application = Flask(__name__)

# low level S3 client to find out number of objects in a bucket
s3client = boto3.client('s3')
buckets = s3client.list_objects(Bucket=BUCKET_NAME)
num_object = len(buckets['Contents'])


@application.route('/')
def index():
    random_num = random.randint(0, num_object - 1)
    obj_key = buckets['Contents'][random_num]['Key']
    object_URI = URI + '/' + obj_key
    return render_template('index.html', object_link=object_URI)


if __name__ == "__main__":
    application.run(host='0.0.0.0', threaded=True)
