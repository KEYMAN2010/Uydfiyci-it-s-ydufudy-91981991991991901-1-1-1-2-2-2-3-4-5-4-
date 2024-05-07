from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/fcf/', methods=['GET'])
def fcf():
    # Get the URL parameter from the request
    link = request.args.get('link')

    if link:
        # Construct the URL for the bypass API with the provided link and API key
        bypass_url = f"http://alpha.embotic.xyz:1195/api/v3/bypass/?url={link}&api_key=Byte_Boulevard_ab2097a1-86bf-4270-9ca4-d3eb262231cc"

        # Make a request to the bypass API
        response = requests.get(bypass_url)

        # Return the response from the bypass API
        return jsonify({"Bypass": response.json()["result"]})

    else:
        # If no link parameter is provided, return an error message
        return jsonify({"error": "No link parameter provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
