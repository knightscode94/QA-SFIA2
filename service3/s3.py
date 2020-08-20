# These will both generate a random “Object”,
# this object can be whatever you like as we encourage creativity in this project.
import random
from flask import Flask, jsonify, request

service3 = Flask(__name__)


    a1 = "As I see it, yes."
    a2 = "Ask again later."
    a3 = "Better not tell you now."
    a4 = "Cannot predict now."
    a5 = "Concentrate and ask again"
    a6 = "Don’t count on it."
    a7 = "It is certain."
    a8 = "It is decidedly so."
    a9 = "Most likely."
    a10 = "My reply is no."
    a11 = "My sources say no."
    a12 = "Outlook not so good."
    a13 = "Outlook good."
    a14 = "Reply hazy, try again."
    a15 = "Signs point to yes."
    a16 = "Very doubtful."
    a17 = "Without a doubt."
    a18 = "Yes."
    a19 = "Yes – definitely."
    a20 = "You may rely on it."


@service3.route('/', methods=['GET'])
def on_get_request():
    return jsonify(answer())


if __name__ == "__main__":
    service3.run(port=5003)