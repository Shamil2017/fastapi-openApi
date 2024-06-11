import requests

url = "http://194.59.40.99:7990/process_text/"

payload = {"text": "Hello, FastAPI!"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
