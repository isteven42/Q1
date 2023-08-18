from flask import Flask, jsonify
import requests

app = Flask(__name__)

def fetch_all_comments():
    url = "https://jsonplaceholder.typicode.com/comments"
    response = requests.get(url)
    return response.json()

def fetch_single_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    return response.json()

def fetch_all_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()

@app.route('/api/comments', methods=['GET'])
def get_all_comments():
    return jsonify(fetch_all_comments())

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_single_post(post_id):
    return jsonify(fetch_single_post(post_id))

@app.route('/api/posts', methods=['GET'])
def get_all_posts():
    return jsonify(fetch_all_posts())

if __name__ == "__main__":
    app.run(debug=True)