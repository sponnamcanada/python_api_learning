import requests


# headers
headers={
    'Accept':'text/plain',
    'content=Type':'application\json'
}


# body to post request
body={
  "id": 125,
  "title": "test from python",
  "dueDate": "2025-03-17T01:54:58.315Z",
  "completed": True
}



# post request with headers and body  if using data when passing use json.dumps)jsonpayload) otherwise use json
response=requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities",headers=headers,json=body)


print(response.status_code)
print(response.json())

data=response.json()
# to test the data or otger use assert
assert response.status_code==200
assert data['id']==125