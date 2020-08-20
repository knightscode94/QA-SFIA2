#This service will also create an “Object” however this “Object” 
# must be based upon the results of service #2 + #3 using some pre-defined rules.





service_2_url = "http://0.0.0.0:5002/"
service_3_url = "http://0.0.0.0:5003/"

get_service_2_response(service_2_url)
get_service_3_response(service_3_url)