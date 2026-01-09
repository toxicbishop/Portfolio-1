from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

# 1. Initialize the Flask App
app = Flask(__name__)

# 2. Enable CORS
# This allows your HTML file (frontend) to talk to this Python script (backend)
CORS(app)

# 3. Connect to Local MongoDB
# 'localhost' means the database is running on this same computer
try:
    client = MongoClient("mongodb://localhost:27017/")
    
    # Create (or connect to) a database named 'portfolio_db'
    db = client['portfolio_db']
    
    # Create (or connect to) a collection (table) named 'messages'
    messages_collection = db['messages']
    print("✅ Successfully connected to local MongoDB!")
except Exception as e:
    print(f"❌ Error connecting to MongoDB: {e}")

# 4. Define the Root Route (Just to check if it works)
@app.route('/')
def home():
    return "Your Local Backend is Running! 🚀"

# 5. Define the Contact Form Route
@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    # Get the data sent from the HTML form
    data = request.json
    
    # Validation: Check if data exists
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Extract fields
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Create the document to save
    new_message = {
        "name": name,
        "email": email,
        "message": message
    }

    # Save to MongoDB
    try:
        messages_collection.insert_one(new_message)
        print(f"📩 New Message Saved: {name} - {email}")
        return jsonify({"message": "Success! Message saved to local DB."}), 200
    except Exception as e:
        print(f"❌ Database Error: {e}")
        return jsonify({"error": "Failed to save to database"}), 500

# --- ADD THIS NEW ROUTE TO app.py ---

@app.route('/get-messages', methods=['GET'])
def get_messages():
    try:
        # 1. Fetch all documents from the database
        # {'_id': 0} tells MongoDB NOT to return the confusing 'ID' field
        messages = list(messages_collection.find({}, {'_id': 0}))
        
        # 2. Return them as a JSON list
        return jsonify(messages), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# 6. Run the Server
if __name__ == '__main__':
    app.run(debug=True, port=5000)