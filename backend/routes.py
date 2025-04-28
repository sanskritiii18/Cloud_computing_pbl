from flask import Flask, jsonify, request
from backend.auth import login_user, register_user

from pymongo import MongoClient
from flask_cors import CORS

server = Flask(__name__)
CORS(server, resources={r"/*": {"origins": "*"}})  # <- Make sure it's like this


client = MongoClient("mongodb://localhost:27017/")
db = client["audioDB"]
collection = db["songs"]

@server.route("/login",methods=["POST"])
def login():
    data =  request.get_json()
    return login_user(data)


@server.route("/register",methods=["POST"])
def register():
    data = request.get_json()
    return register_user(data)


@server.route('/search', methods=['GET'])
def search_songs():
    query = request.args.get('query', '').strip()
    if not query:
        return jsonify([])

    print(f"Query: {query}")
    try:
        results = collection.find({
            "title": {"$regex": query, "$options": "i"}
        })

        results = list(results)
        print(f"Results found: {len(results)}")

        output = []
        for song in results:
            title = song.get("title")
            url = song.get("url")
            image_url = song.get("image_url")
            if title and url and image_url:
                output.append({"title": title, "url": url,"image_url":image_url})
        print("Final Output:", output)

        return jsonify(output)


    except Exception as e:
        print(f"Error in /search: {e}")
        return jsonify({"error": "Server error occurred"}), 500

if __name__ == "__main__":
    server.run(debug=True, port=5050)
