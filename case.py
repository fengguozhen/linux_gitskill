import requests
url = "https://www.baidu.com"
r =requests.request("GET",url=url)

print(r.text())
print(r.state_code())
