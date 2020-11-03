import boto3

# =======================================================
# Boto3 resource is more low-level-control than Boto3 client
# =======================================================

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='QueueName')
print(queue)

# =======================================================
# Boto3 client is simpler than Boto3 resource
# =======================================================

# Get the service client
sqs_client = boto3.client('sqs')

# List SQS queues
response = sqs_client.list_queues()

print(response['QueueUrls'])
