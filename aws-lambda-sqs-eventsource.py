# ==========================================================================================
# Filename:     aws-lambda-sqs-eventsource.py
# Description:  AWS Lambda Python code to use SQS event source.
#               Setup Lambda trigger to point to SQS queue.
# ==========================================================================================


def lambda_handler(event, context):
    '''
    Use SQS event source, print to console.
    
    The SQS event json has key 'Records', where value is list with a single item.
    
    The single item is an embedded json with keys
     * 'body': the value is str message
     * 'messageAttributes': the value is json/dict
            - Keys are messageAttribute names
                - Values are embedded json/dict
                    - 'stringValue' -> string with message attribute value
                    - 'dataType' -> string where possible values are: 'String', 'Number'
                    - stringListValues' -> empty list, according to AWS documentation reserved for future use
                    - 'binaryListValues' -> empty list, according to AWS documentation reserved for future use
                    
    Reference:
     * # https://docs.aws.amazon.com/cli/latest/reference/sqs/send-message.html
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
    
