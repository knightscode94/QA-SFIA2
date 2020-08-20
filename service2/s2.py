#These will both generate a random “Object”, 
# this object can be whatever you like as we encourage creativity in this project.
import random
from flask import Flask, jsonify, request

service2 = Flask(__name__)

def number():
    ans = random.randint(1, 20)

    return ans

@service2.route('/', methods=['GET'])
def on_get_request():
    return jsonify(number())


if __name__ == "__main__":
    service2.run(port=5002)