import requests
import json

# Flask API URL
flask_api_url = 'http://your-flask-api-url/prompt'

# Azure OpenAI API URL
openai_api_url = 'https://api.openai.com/v1/engines/davinci-codex/completions'

# Set up your OpenAI API credentials
openai_api_key = 'YOUR_OPENAI_API_KEY'

# Define the prompt
prompt = {
    "prompt": "What is the projected tax percentage for the state of California for Alternative Minimum Tax (AMT) rate next year?",
    "examples": [
        {"prompt": "What is the projected tax percentage for the state of New York for Sales Tax rate next year?"},
        {"prompt": "What is the projected tax percentage for the state of Texas for Property Tax rate next year?"}
    ]
}

# Convert prompt to JSON
prompt_json = json.dumps(prompt)

# Call Flask API with 'PROMPT' method
response1 = requests.request('PROMPT', url=flask_api_url)

# Print the response from Flask API
print(response1.json())

# Call Azure OpenAI API. #TODO udpate for the azure open ai with additional parameters
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {openai_api_key}'
}

response2 = requests.post(openai_api_url, headers=headers, data=prompt_json)

# Get the response from Azure OpenAI API
response2_data = response2.json()

# Extract the generated completion from Azure OpenAI API response
completion = response2_data['choices'][0]['text']

# Call Flask API again with the generated completion
response3 = requests.post(flask_api_url, json={'completion': completion})

# Print the response from the second call to Flask API
print(response3.json())
