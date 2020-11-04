# ==========================================================================================
# Filename:     aws-sqs-create-send.py
# Description:  AWS Lambda/Boto3 Python code to create SQS queue and send SQS messages.
#               Separately another Lambda will use the SQS queue as event source.
# ==========================================================================================

import json
import boto3
import time

# Get the service client
sqs = boto3.client('sqs')
    
def ls_sqs_queue():
    '''
    Print out list of SQS queue URLs and names.  Return as output.
    
    Create the boto3 SQS client object.  Run .list_queues() method.
    The response is a json with key 'QueueURLs'.
    The name of SQS Queue is last part of URL, after '/'.
    Print out the entire SQS queue URL and parsed queue name. 
    
    Return:
        * ls_sqs_queue_urls - list, SQS queue URLs
        * ls_sqs_queue_names - - list, SQS queue names
    '''
    
    # List SQS queues
    response = sqs.list_queues()
    ls_sqs_queue_urls = response['QueueUrls']
    ls_sqs_queue_names = [x.split('/')[-1] for x in ls_sqs_queue_urls]
    
    print()
    print('SQS queue URLs: ', ls_sqs_queue_urls)
    print()
    print('SQS queue names: ', ls_sqs_queue_names)
    print()
    
    return ls_sqs_queue_urls, ls_sqs_queue_names
    
    
def send_sqs_msg(queue_url, str_msg_ticker):
    '''
    Send message to SQS queue.
    '''
    
    # Send message to SQS queue
    # (included optional MessageAttributes)
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            'Attribute1_str': {
                'DataType': 'String',
                'StringValue': 'value of Attribute1_str'
            },
            'Attribute2_str': {
                'DataType': 'String',
                'StringValue': 'value of Attribute2_str'
            },
            'Attribute3_num': {
                'DataType': 'Number',
                'StringValue': '3'
            }
        },
        MessageBody=(str_msg_ticker)
    )
    
    
def lambda_handler(event, context):
    '''
    This lambda will provide background SQS setup.
     * Setup SQS queue.
     * Write list of messages to SQS.
     
    Then another lambda will use SQS queue as event source.
    
    References:
     * https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs-examples.html
     * https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs-example-using-queues.html
     * https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs-example-sending-receiving-msgs.html
     * https://aws.amazon.com/blogs/developer/using-python-and-amazon-sqs-fifo-queues-to-preserve-message-sequencing/
    '''
    
    # check on list of SQS queue names
    ls_sqs_queue_urls, ls_sqs_queue_names = ls_sqs_queue()
    
    # Create a SQS queue if it doesn't exist
    str_queue_create = 'QUEUE_NAME_STRING' 
    if str_queue_create not in ls_sqs_queue_names:
        response = sqs.create_queue(
            QueueName=str_queue_create,
            Attributes={
                'DelaySeconds': '60',
                'MessageRetentionPeriod': '86400'
            }
        )
        time.sleep(30)
        
    # save queue URL in order to send message
    idx_queue_create = ls_sqs_queue_names.index(str_queue_create)
    queue_url = ls_sqs_queue_urls[idx_queue_create]
    
    # create list of messages ... in future version, this list of messages can be pulled from DynamoDB
    ls_str_msgs = ['msg1', 'msg2', 'msg3']
    
    # send messages from list
    for each_msg in ls_str_msgs:
        send_sqs_msg(queue_url, each_msg)
        print('Created SQS message: ', each_msg)
    
    
