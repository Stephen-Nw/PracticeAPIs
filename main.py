import requests


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (longitude, latitude)

print(iss_position)



# print(response.status_code)
# Response.raise_for_status() will raise an HTTPError if the HTTP request returned an unsuccessful status code.