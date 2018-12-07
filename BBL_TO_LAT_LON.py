import requests
import os

# Set key and id as enviornment variables
# os.environ['NYC_GEOCLIENT_ID']
# os.environ['NYC_GEOCLIENT_KEY']

def get_lat_lon_from_bin(bin_number):
    
    base_url = 'https://api.cityofnewyork.us/geoclient/v1/bin.json'
    api_id = os.environ['NYC_GEOCLIENT_ID']
    api_key = os.environ['NYC_GEOCLIENT_KEY']
    
    PARAMS = {'bin':bin_number, 'app_id':api_id, 'app_key':api_key}
    output = (requests.get(url = base_url, params = PARAMS)).json()
    
    return (output['bin']['latitudeInternalLabel'], output['bin']['longitudeInternalLabel'])

def get_lat_lon_from_bin_array(bin_numbers):
    
    base_url = 'https://api.cityofnewyork.us/geoclient/v1/bin.json'
    api_id = os.environ['NYC_GEOCLIENT_ID']
    api_key = os.environ['NYC_GEOCLIENT_KEY']
    result = []
    
    for bin_number in bin_numbers:
        PARAMS = {'bin':bin_number, 'app_id':api_id, 'app_key':api_key}
        output = (requests.get(url = base_url, params = PARAMS)).json()
        result.append( (output['bin']['latitudeInternalLabel'], output['bin']['longitudeInternalLabel']) )

    return result
