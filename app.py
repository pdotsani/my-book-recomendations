from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
from pymongo import MongoClient
import os
import random
load_dotenv()

app = Flask(__name__)

# MongoDB connection
mongodb_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
db_name = os.getenv("MONGODB_DB", "book_recommendations")
collection_name = os.getenv("MONGODB_COLLECTION", "books")
client = MongoClient(mongodb_uri, tlsAllowInvalidCertificates=True)
db = client[db_name]
collection = db[collection_name]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/get-recomendation', methods=['GET'])
def get_recomendation():
    try:
        # Get a random document from the collection using aggregation
        pipeline = [{"$sample": {"size": 1}}]
        random_books = list(collection.aggregate(pipeline))
        
        if not random_books:
            return jsonify({"error": f"Collection '{collection_name}' is empty"}), 500
        
        random_book = random_books[0]
        
        # Extract title and cover
        title = random_book.get("title", "Unknown Title")
        cover = random_book.get("cover", "")
        
        return jsonify({
            "title": title,
            "cover": cover
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

