import requests
import json
from random import randint
from time import sleep


url0 = "https://ddc.fis.vn/fis0/api/login"
headers0={"Host": "ddc.fis.vn",
"Content-Type": "application/json",
"Content-Length": "166",
"Accept-Encoding": "gzip, deflate",
"User-Agent": "okhttp/4.9.1",
"Connection": "close"}

data0={"username":"duydv25","password":"Duc@tiHyper950",
"buildNumber":"10955","version":"1.85","deviceIP":"10.15.180.1",
"deviceModel":"iPhone14,2","osVersion":"16.3"}

response = requests.post(url0, headers=headers0, json=data0)

print("Status Code", response.status_code)
print("JSON Response ", response.json())


data=response.json()


token="Bearer" +" "+ data.get('data').get('token')
#print(token)
url1 = "https://ddc.fis.vn/fis0/api/checkout_all"
 
headers1 = { "Host": "ddc.fis.vn",
"Authorization": token,
"Content-Type": "application/json",
"Content-Length": "265",
"Accept-Encoding": "gzip, deflate",
"User-Agent": "okhttp/4.9.1",
"Connection": "close"}
 
data1 = {"deviceId":"C09EFE06-56E7-4F23-90DE-FDB4721532F0","ssid":"FIS","deviceName":"iPhone14,2","ipGateway":"10.15.180.1","type":0,"dataPrivate":"MiSXyUe6HnJW7CXHrsYUYI/1MJMyQmlMcypAQIz6+l6cEz7CJhQT4E8yPtie+m5WttfWpvc2K0xG\nfUrhMm8uzMeauvQR1GYB0ws2YBECdPXNyHJEYTI/cdxwkfy4RP/vku8HSfP8m4t9AaTeVEhtZ0yM\nwVmi6RK7YO1t4B+7W8A=\n"}
 
response = requests.post(url1, headers=headers1, json=data1)
 
print("Status Code", response.status_code)
print("JSON Response ", response.json())