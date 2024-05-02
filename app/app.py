from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import os
import subprocess
import urllib.request

# Initialize the Flask application and Flask-RESTful API
app = Flask(__name__)
api = Api(app)

class Print(Resource):
    def post(self):
        # Retrieve JSON data from the request
        json_data = request.get_json()
        if not json_data:
            return {"error": "No data in request"}, 400

        # Extract text fields and image URL from the JSON data
        text1 = json_data.get("text1")
        text2 = json_data.get("text2")
        text3 = json_data.get("text3")
        text4 = json_data.get("text4")
        img_url = json_data.get("img_url")
        qr = json_data.get("qr")

        # Check if at least one of text1, qr, or img_url is present
        if not any([text1, qr, img_url]):
            return {"error": "Require at least one of the arguments text1, qr, or img_url"}, 400


        # Prepare the command for the label printing subprocess
        print_command = ["labelle"]
        if img_url:
            try:
                img_path = os.path.join(app.root_path, "img.jpg")
                # Remove existing image to prevent reuse
                if os.path.exists(img_path):
                    os.remove(img_path)
                urllib.request.urlretrieve(img_url, img_path)
                print_command += ['--picture', img_path]
            except Exception as e:
                return {"error": f"Failed to process image: {e}"}, 500

        if qr:
            print_command += ['--qr', qr]

        # Append text fields to the command
        print_command += [text1]
        if text2:
            print_command += [text2]
        if text3:
            print_command += [text3]
        if text4:
            print_command += [text4]

        # Execute the print command using subprocess safely
        try:
            output = subprocess.check_output(print_command, text=True)
        except subprocess.CalledProcessError as e:
            return {"error": f"Printing failed: {e.output}"}, 500

        # Return the result from the subprocess execution
        return {"message": output}

class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World!"}

# Register resources with the endpoints
api.add_resource(HelloWorld, "/hello")
api.add_resource(Print, "/print")

if __name__ == "__main__":
    # Start the Flask app
    app.run(host='0.0.0.0', port=5001, debug=True)
