from flask import Flask, request
from github_utils import comment_on_pr
from review import generate_review
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data.get("action") == "opened" and "pull_request" in data:
        pr_url = data["pull_request"]["url"]
        diff_url = data["pull_request"]["diff_url"]
        review_comment = generate_review(diff_url)
        comment_on_pr(pr_url, review_comment)
    return '', 204

if __name__ == '__main__':
    app.run(port=5000)
