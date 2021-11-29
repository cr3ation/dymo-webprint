from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import json
import os
import urllib.parse


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
        
        text1 = urllib.parse.quote(json_data["text1"])
        text2 = urllib.parse.quote(json_data["text2"])

        shell_command = '/usr/local/bin/dymoprint "{0}" "{1}"'.format(text1, text2)

        print_output = os.popen(shell_command).read()
        if print_output:
            result = '{"message": "something went horrobly wrong!"}'
            return(json.loads(result), 500)
        print(print_output)
        return(json.loads('{ "message": "True" }'))


class HelloWorld(Resource):
    def get(self):
        return("Hello, World!")


api.add_resource(HelloWorld, "/hello")
api.add_resource(Print, "/print")
#api.add_resource(Print, "/print/<string:text1>")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
