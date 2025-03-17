# //importing the requests module 
import requests

# adding the headers
headers={

    'Accept':'text/plain'
}

# hitting the get requests url and stroing the response
response=requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities",headers=headers)

response2=requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities")
# printing the json putput 
print(response.json())



# [printing the status]
print(response.status_code)


print(response2.json())


