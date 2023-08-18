from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def fetch_all_comments():
    url = "https://jsonplaceholder.typicode.com/comments"
    response = requests.get(url)
    return response.json()

@app.route('/api/search_comments', methods=['GET'])
def search_comments():
    # Fetch all comments
    comments = fetch_all_comments()

    # Filter based on query parameters
    for key, value in request.args.items():
        comments = [comment for comment in comments if str(comment.get(key)) == value]
    
    return jsonify(comments)

if __name__ == "__main__":
    app.run(debug=True)