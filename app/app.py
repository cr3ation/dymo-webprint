from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

# Create webapp
app = Flask(__name__)
api = Api(app)

# Limitations per host per day / hour
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["500 per day", "120 per hour"])


class Print(Resource):
    def get(self, text1):
        data = text1
        if not data:
            # Nothing to return
            return("", 204)
        print_output = os.popen('/usr/local/bin/dymoprint "{0}"'.format(text1)).read()
        print(print_output)
        return(data)


class HelloWorld(Resource):
    def get(self):
        return("Hello, World!")


api.add_resource(HelloWorld, "/hello")
api.add_resource(Print, "/print/<string:text1>")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
