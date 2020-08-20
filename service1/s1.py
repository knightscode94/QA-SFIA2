import requests
from flask import Flask, jsonify

service1 = Flask(__name__)

def get_service_2_response(url):

    service_2_response = requests.get(url)
    decoded_service_2_response = service_2_response.json()

    print("\n ----------- Service 2 GET Response ----------- \n")
    print(decoded_service_2_response)
    print("\n ----------- Service 2 GET Response ----------- \n")

    return decoded_service_2_response

#### userinput /form /user interface

# TODO: Do this

##################################################################



if __name__ == "__main__":
    service1.run(port=5001)