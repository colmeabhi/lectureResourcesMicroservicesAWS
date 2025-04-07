curl -X POST https://your-api-id.execute-api.us-east-1.amazonaws.com/OrderService \
  -H "Content-Type: application/json" \
  -d '{"userId": "returned-user-id", "book": "Clean Code", "quantity": 1}'
