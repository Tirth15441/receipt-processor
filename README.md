## Overview
This project implements a Flask-based API to process receipts and calculate points based on predefined rules. It uses Docker for containerization.

## Features
1. POST `/receipts/process`: Processes a receipt and returns a unique ID.
2. GET `/receipts/{id}/points`: Returns the points awarded for a receipt.

## How to Run the Application

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd receipt-processor


###2. Run Using Docker
Build the Docker image:


docker build -t receipt-processor .
Run the container:


docker run -p 5000:5000 receipt-processor


###Access the application:

POST: http://127.0.0.1:5000/receipts/process
GET: http://127.0.0.1:5000/receipts/{id}/points


###3. Test the API
Use Postman or curl to test the endpoints.

4. Example JSON Inputs
POST /receipts/process:

{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    { "shortDescription": "Mountain Dew 12PK", "price": "6.49" },
    { "shortDescription": "Emils Cheese Pizza", "price": "12.25" }
  ],
  "total": "18.74"
}
