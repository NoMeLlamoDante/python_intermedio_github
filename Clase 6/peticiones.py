import requests
import os
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print("="*50)
print(type(response.text))
print(response.text)
print("="*50)
print(response.json())
print(type(response.json()))

response_dic = response.json()


for key, value in response_dic.items():
    print(f"key => {key}, value => {value}")