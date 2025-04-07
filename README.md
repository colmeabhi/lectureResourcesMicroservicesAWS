# 📚 Lecture Plan: Microservices in the Cloud (AWS)

## 🎯 Objective

Help students understand what microservices are, why they’re useful, and how to implement a basic microservices architecture using **AWS**.

---

## ☁️ PART 1: Cloud Implementation on AWS

### 📦 Microservices Infrastructure Components

| Component       | AWS Service         | What it does                                |
|----------------|---------------------|----------------------------------------------|
| Microservices   | AWS Lambda          | Serverless compute for each service          |
| API Gateway     | Amazon API Gateway  | Front door to your services                  |
| Data Layer      | Amazon DynamoDB     | NoSQL database for microservices             |
| Communication   | Amazon SNS/SQS      | Async event messaging                        |
| Monitoring      | Amazon CloudWatch   | Logs and metrics                             |
| Security        | IAM Roles + VPC     | Access control and isolation                 |

---

## 🛠️ PART 2: The Demo Project – Book Order App

### 💡 Use Case
- User registers via `/UserService`
- User places an order via `/OrderService`
- System sends confirmation email via **SNS**

---

## 🪜 PART 3: Step-by-Step Setup (Hands-on)

### 🔹 Step 1: Create DynamoDB Tables
- **UserTable** → Partition Key: `userId` (String)  
- **OrderTable** → Partition Key: `orderId` (String)

---

### 🔹 Step 2: Create SNS Topic
- Name: `OrderNotifications`
- Create an **email subscription**
- Confirm it via inbox (verify student email)

---

### 🔹 Step 3: Create 2 Lambda Functions

- **`UserService` Lambda**:  
  - Python code available in `user_service_code.py`  
- **`OrderService` Lambda**:  
  - Python code available in `order_service_code.py`  

> ⚠️ **Note**: For simplicity, attach full access policies to both Lambdas:
- `AmazonDynamoDBFullAccess`
- `AmazonSNSFullAccess`  
(Not production best practices, but perfect for teaching.)

---

### 🔹 Step 4: Set Up API Gateway (HTTP API)

1. Create a new **HTTP API**
2. Add 2 routes:
   - `POST /UserService` → Integrate with `UserService Lambda`
   - `POST /OrderService` → Integrate with `OrderService Lambda`
3. Deploy to a stage (`$default`)
4. Note your base URL: https://your-api-id.execute-api.us-east-1.amazonaws.com (Use your own URL from console!!!)

---

### 🔹 Step 5: Test the Endpoints

Use **curl** or **Postman** to test:

- **Create User**  
- Command: See `curl_commands_create_user.sh`  
- Edit it with your API URL and parameters  

- **Place Order**  
- Command: See `curl_commands_place_order.sh`  
- Update it with a real `userId` and API URL  

> 💡 Run the curl commands in your terminal to see the microservices work together live!

---

## 🧠 That’s It!

You’ve now:
- Built serverless microservices
- Used real AWS tools (Lambda, API Gateway, DynamoDB, SNS)
- Created a real-world cloud-native app
