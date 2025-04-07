import json, uuid, boto3
dynamo = boto3.resource('dynamodb')
table = dynamo.Table('UserTable')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    user_id = str(uuid.uuid4())
    table.put_item(Item={'userId': user_id, 'name': body['name'], 'email': body['email']})
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'User created', 'userId': user_id})
    }
