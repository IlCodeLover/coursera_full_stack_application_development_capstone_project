# Uncomment the imports below before you add the function code
# import requests
import os

import requests
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# TO DO: Add code for get requests to back end
def get_request(endpoint, **kwargs):
    """
    get request function constructs a URL with query paramater
    and make GET request to the Nodeapp backend service.
    :param endpoint: the url
    :param kwargs: python keyword arguments represeting all URL parameters to be associated with the get call
    :return: response
    """
    params=""
    if(kwargs):
        for key, value in kwargs.items():
            #params= params + key + "=" + value + "&"
            params += f"{key}={value}&"
        params = params.rstrip(('&'))

    request_url = backend_url + endpoint
    if(params):
        request_url = request_url + "?" + params
    print("GET from {} ".format(request_url))

    try:
        # call get method of requests library with URL and params
        response = requests.get(request_url)
        return response.json()
    except requests.exceptions.RequestException as err:
        # if any error occurs
        print(f"Network exception occurred: {err}")

# TO DO: Add code for consume the micro service to analyze sentiments
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of request library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred.")

# Add code for posting review
def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
