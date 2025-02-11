import requests
import json
from .models import CarDealer
from requests.auth import HTTPBasicAuth

def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    json_data = "Error_self"
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
        status_code = response.status_code
        print("With status {} ".format(status_code))
        json_data = json.loads(response.text)
    except:
        # If any error occurs
        print("Network exception occurred")
    return json_data



def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        print('response',json_result)
        # dealers = json.loads(json_result)
        
        # For each dealer object
        # for dealer in dealers:
        #     # Get its content in `doc` object
        #     dealer_doc = dealer
        #     print("DEaler",dealer_doc)
        #     # Create a CarDealer object with values in `doc` object
        #     dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
        #                            id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
        #                            short_name=dealer_doc["short_name"],
        #                            st=dealer_doc["st"], zip=dealer_doc["zip"])
        #     results.append(dealer_obj)

    return json_result