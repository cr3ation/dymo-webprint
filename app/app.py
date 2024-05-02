from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import os
import subprocess
import urllib.request

# Create webapp
app = Flask(__name__)
api = Api(app)

class Print(Resource):
    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"error": "no data in request"}, 400

        text1 = json_data.get("text1")
        text2 = json_data.get("text2")
        text3 = json_data.get("text3")
        text4 = json_data.get("text4")
        img_url = json_data.get("img_url")
        qr = json_data.get("qr")

        print_command = "labelle"
        if img_url:
            img_path = os.path.join(app.root_path, "img.jpg")
            if os.path.exists(img_path):
                os.remove(img_path)
            urllib.request.urlretrieve(img_url, img_path)
            print_command += f' --picture "{img_path}"'
        if qr:
            print_command += f' --qr "{qr}"'
        if not text1:
            return {"error": "text1 parameter missing in request"}, 400
        print_command += f' "{text1}"'
        if text2:
            print_command += f' "{text2}"'
        if text3:
            print_command += f' "{text3}"'
        if text4:
            print_command += f' "{text4}"'

        # Print using safe subprocess call
        print(f"Command to execute: {print_command}")
        output = subprocess.getoutput(print_command)

        # Return
        return {"message": output}

class HelloWorld(Resource):
    def get(self):
        return "Hello, World!"

api.add_resource(HelloWorld, "/hello")
api.add_resource(Print, "/print")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
