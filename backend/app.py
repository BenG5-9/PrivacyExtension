from flask import Flask, jsonify, request
from extract_policy import extract_policy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.get_json()['url']
        print(url)
        return extract_policy(url)
    
    else:

        return "invalid request"

if __name__ == "__main__":
    app.run(port=8000)