from flask import Flask, render_template, request
import os
import config
import csv



HOST_NAME = 's3-ap-southeast-2.amazonaws.com/'
BUCKET_NAME = 'meme-generator-source' # replace with your bucket name


application = Flask(__name__)

#Loads access and secret keys from local rootkey_file
IAM_PATH = config.FILE_PATH
rootkey_file = csv.reader(open(IAM_PATH + 'rootkey.csv'))
keys = list(rootkey_file)
accss_keys = keys[0][0].split("=")[1]
secret_keys = keys[1][0].split("=")[1]


@application.route('/')
def index():

	return render_template('index.html')


if __name__ == "__main__":
	application.run(host = '0.0.0.0', threaded=True)


def generateAuthorization(access, secret): #construct Authrorization required for REST requests 
	#format = Authorization : AWS AWSAccessKeyId:Signature
	Signature = Base64(HMAC-SHA1(secret, UTF-8-Encoding-Of( StringToSign ) ) );
	Authorization = "AWS" + " " + access + ":" + Signature;




