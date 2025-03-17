import requests,json

url="https://fakerestapi.azurewebsites.net/api/v1/Activities"

headers={
    'Accept':'text/plain',
    'content=Type':'application\json'
}

json_file=open('./jsonpayload.json')

body=json.load(json_file)

response=requests.post(url,headers=headers,json=body)

print(response.status_code)