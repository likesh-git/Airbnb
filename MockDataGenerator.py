import json
from dotenv import load_dotenv
import logging 
import os
import boto3
import random
import string
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)
load_dotenv()

def data_generator():
    message = {
    "bookingId":str(random.randint(10000,99999)) ,
    "userId":''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)),
    "propertyId":''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)),
    "location":random.choice(["Tampa, Florida","Hyd, Ind","BLR, Ind"]),
    "startDate":random.choice(["2024-03-12","2024-03-13","2024-03-14"]),
    "endDate":random.choice(["2024-03-13","2024-03-14","2024-03-15"]),
    "price":'$' + str(random.randint(100,999))
    }
    return message

def lambda_handler(event, context):
    
    sqs_url = os.getenv('sqs_url')
    sqs_client = boto3.client('sqs')
    sample_data = data_generator()
    for i in range(25):
        sqs_client.send_message(QueueUrl = sqs_url, MessageBody = json.dumps(data_generator()))
        time.sleep(1)
        
    logger.info('Data published')
    return 
