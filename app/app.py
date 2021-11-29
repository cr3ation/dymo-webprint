from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import json
import os
import subprocess as sp
import urllib.request

# Create webapp
app = Flask(__name__)
api = Api(app)

# Limitations per host per day / hour
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["500 per day", "120 per hour"])


class Print(Resource):        
    def post(self):
        json_data = request.get_json()
        if not json_data:
            # Nothing to return
            return(json.loads('{ "error": "no data in request" }'), 400)

        # Get parameters from request
        text1 = json_data["text1"] if "text1" in json_data else None
        text2 = json_data["text2"] if "text2" in json_data else None
        img_url = json_data["img_url"] if "img_url" in json_data else None
        qr = json_data["qr"] if "qr" in json_data else None

        # Build print command
        print_command = '/usr/local/bin/dymoprint "{0}"'.format(text1)        
        if not text1:
            return(json.loads('{ "error": "text1 parameter missing in request" }'), 400)
        print_command = '{0} {1}'.format(print_command, text1)
        if text2:
            print_command = '{0} "{1}"'.format(print_command, text2)
        if qr:
            print_command = '{0} --qr "{1}"'.format(print_command, qr)
        if img_url:
            img_path = os.path.dirname(os.path.abspath(__file__)) + "/img.jpg"
            if os.path.exists(img_path):
                os.remove(img_path)
            urllib.request.urlretrieve(img_url, img_path)
            print_command = '{0} --picture "{1}"'.format(print_command, img_path)
 
        # Print
        output = sp.getoutput(print_command)

        # Return
        info = '{ "message": "%s}" }' % output
        return(json.loads(info))


class HelloWorld(Resource):
    def get(self):
        return("Hello, World!")


api.add_resource(HelloWorld, "/hello")
api.add_resource(Print, "/print")
#api.add_resource(Print, "/print/<string:text1>")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
