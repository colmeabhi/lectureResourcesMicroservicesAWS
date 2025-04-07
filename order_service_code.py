import json, uuid, boto3
dynamo = boto3.resource('dynamodb')
sns = boto3.client('sns')
order_table = dynamo.Table('OrderTable')
SNS_TOPIC_ARN = 'arn:aws:sns:REGION:ACCOUNT_ID:OrderNotifications'

def lambda_handler(event, context):
    body = json.loads(event['body'])
    order_id = str(uuid.uuid4())
    order_table.put_item(Item={
        'orderId': order_id,
        'userId': body['userId'],
        'book': body['book'],
        'quantity': body['quantity']
    })
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=f"Order placed: {body['book']} (x{body['quantity']})",
        Subject="Book Order Confirmation"
    )
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Order placed', 'orderId': order_id})
    }
