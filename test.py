import requests

response = requests.get("https://dog.ceo/api/breeds/image/random")

print("Status:", response.status_code)
print("Headers:")
for k, v in response.headers.items():
    print(f"{k}: {v}")