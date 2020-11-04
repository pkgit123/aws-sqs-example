# ==========================================================================================
# Filename:     aws-lambda-sqs-eventsource.py
# Description:  AWS Lambda Python code to use SQS event source.
#               Setup Lambda trigger to point to SQS queue.
# ==========================================================================================


def lambda_handler(event, context):
    '''
    Use SQS event source, print to console.
    
    The SQS event json has key 'Records', where value is list with single item.
    The single item is an embedded json with key 'body'; the value is str message.
    '''
    
    # Event Source: SQS message body
    str_sqs_body = event['Records'][0]['body']
    
    # Event Source: SQS message attributes
    di_sqs_messageattributes = event['Records'][0]['messageAttributes']
    
    print('str_sqs_body: ', str_sqs_body)
    print()
    print('di_sqs_messageattributes: ', di_sqs_messageattributes)
    print()
    print('Event: ', event)
    print()
    
