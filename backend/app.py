from flask import Flask, jsonify, request, session
from extract_policy import extract_policy
from opt_out import send_opt_out
from flask_cors import CORS
from AI import getSummary, getOptOut

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get url from request
        url = request.get_json()['url']

        # find the policy
        policy = extract_policy(url)

        # Alan processes policy using the power of AI
        if policy != "No policy found":

            summary = getSummary(policy)
            opt = getOptOut(policy)
            
            if(opt != None):
                send_opt_out(opt, "I wish to opt out of any optional data collection or processing")
            
            return summary

        # return modified data to be posted to the extension
        return policy
    
    else:

        return "none"

if __name__ == "__main__":
    app.run(port=8000)