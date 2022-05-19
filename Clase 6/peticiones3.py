import requests
import os
os.system('cls')
response = requests.get("https://jsonplaceholder.typicode.com/users")

print("="*50)
print(type(response.text))
print(response.text)
print("="*50)
print(response.json())
print(type(response.json()))

response_dic = response.json()

for data in response_dic:
    print(data)