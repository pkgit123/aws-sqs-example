# aws-sqs-example
Playbook of working with AWS SQS queue

When triggering an AWS Lambda Function (serverless compute), it requires an event input.  For some events such as S3 uploads, the Lambda trigger is relatively straightforward.  But for certain types of CloudWatch triggers, might be better to use SQS queue.  

### References: 
* https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs-examples.html
* https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs-example-using-queues.html
* https://aws.amazon.com/blogs/developer/using-python-and-amazon-sqs-fifo-queues-to-preserve-message-sequencing/
