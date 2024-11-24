from flask import Flask, request, jsonify
import uuid
from points_calculator import calculate_points

app = Flask(__name__)

# POST route to process receipts
@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    data = request.json
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    # Logic to process receipt and return an ID
    return jsonify({"id": "sample-id"})

# GET route to fetch points for a specific receipt
@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
    # Logic to retrieve points for the given receipt_id
    return jsonify({"points": 42})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

