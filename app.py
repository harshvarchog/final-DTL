from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage (replace with a database later)
sensor_data = []

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    if not data or 'temperature' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    data['timestamp'] = datetime.utcnow().isoformat()
    sensor_data.append(data)
    print("Received:", data)  # Log to Render dashboard
    return jsonify({"message": "Data stored"}), 200

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(sensor_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
