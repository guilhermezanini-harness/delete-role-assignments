# Harness Role Assignment Deletion Script

## Overview

This Python script is designed to automate the deletion of role assignments in the Harness platform using the Harness REST API. It reads a list of role assignment identifiers from a JSON file and sends DELETE requests for each identifier to the specified API endpoint.

## Prerequisites

Before using this script, ensure that you have the following prerequisites:

1. **Python (Python 3.6 or higher)**: The script is written in Python, so you must have Python 3.6 or higher installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

2. **Requests Library**: The script uses the `requests` library for making HTTP requests. You can install it using `pip`:

   ```
   pip install requests
   ```

3. **Harness API Key**: You will need a valid Harness API key with the necessary permissions to delete role assignments. Ensure that you have your API key ready.

4. **Account Identifier**: You should know the account identifier for the Harness account where you want to delete role assignments.

## Usage

1. Clone or download this repository to your local machine.

2. Set the following environment variables:
   - `HARNESS_API_KEY`: Your Harness API key.
   - `HARNESS_ACCOUNT_IDENTIFIER`: The account identifier for your Harness account.

   Example (Linux/macOS):
   ```bash
   export HARNESS_API_KEY=YOUR_API_KEY_HERE
   export HARNESS_ACCOUNT_IDENTIFIER=YOUR_ACCOUNT_IDENTIFIER_HERE
   ```

3. Create a JSON file named `role_assignments.json` containing a list of role assignment identifiers that you want to delete. Example:

   ```json
   ["role_assignment_1", "role_assignment_2", "role_assignment_3"]
   ```

4. Run the script:

   ```bash
   python delete_role_assignments.py
   ```

5. The script will iterate through the list of identifiers and send DELETE requests for each one. It will display success or failure messages for each request.

## Customization

You can customize the script by modifying the following variables in the script:

- `API_KEY`: If you want to hardcode your API key instead of using an environment variable.

## Disclaimer

This script is provided as-is and without warranty. Use it responsibly and at your own risk. Be cautious when deleting role assignments, as it may have significant consequences on your Harness Access Control.
