import os
import requests

api_key = os.environ.get("a54f5e809d19b466ea9473efa696d098")

if api_key is None:
    raise Exception("API_KEY environment variable is not set.")

# Now you can use the 'api_key' variable in your code

