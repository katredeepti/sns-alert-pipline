import boto3
client = boto3.client('sns')

def lambda_handler(event, context):
    client.publish(
    TopicArn='arn:aws:sns:us-east-2:992014891278:prod_stop_notification',
    Message='prod server is stopped pls action on it please check it
    i am changing it ',
    )
