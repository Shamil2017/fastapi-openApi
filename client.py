import requests

url = "http://194.59.40.99:7990/process_text/"

system_content = "Вы психолог, специализирующийся на детях"
user_content = "Помогите мне правильно воспитать дочь. Она со мной спорит. Я ее наказываю. Дай ответ на русском языке"

payload = {"system_content": system_content, "user_content": user_content}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.json()["response"])