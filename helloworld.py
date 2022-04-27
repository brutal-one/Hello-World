import requests

msg = "Hello World!"
print(msg)
print(msg)

r = requests.get("tower.crowe.local")

print('r.status_code')