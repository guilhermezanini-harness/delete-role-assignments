import json
import os
import requests

# Retrieve the API key and account identifier from environment variables
API_KEY = os.environ.get('HARNESS_API_KEY')
ACCOUNT_IDENTIFIER = os.environ.get('HARNESS_ACCOUNT_IDENTIFIER')

if not API_KEY:
    raise ValueError("HARNESS_API_KEY environment variable not set. Please set the API key.")
if not ACCOUNT_IDENTIFIER:
    raise ValueError("HARNESS_ACCOUNT_IDENTIFIER environment variable not set. Please set the account identifier.")

# Load the JSON file containing the list of identifiers
with open('role_assignments.json', 'r') as json_file:
    role_assignments = json.load(json_file)

# Base URL for the API endpoint
base_url = 'https://app.harness.io/authz/api/roleassignments/'

# Iterate through the list of identifiers and execute DELETE request for each
for identifier in role_assignments:
    # Construct the full URL with the identifier and accountIdentifier
    url = f"{base_url}{identifier}?accountIdentifier={ACCOUNT_IDENTIFIER}"
    
    try:
        # Send the DELETE request using the requests library
        response = requests.delete(url, headers={'x-api-key': API_KEY})
        
        # Check the response status code and handle as needed
        if response.status_code == 200:
            print(f"Role assignment {identifier} deleted successfully.")
        else:
            raise Exception(f"Failed to delete role assignment {identifier}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to delete role assignment {identifier}. Error: {str(e)}")
        break  # Stop processing on the first request failure

print("All role assignments processed.")