import requests
import json
import secret
 
url_template = 'https://api.foursquare.com/v2/users/self/checkins?limit=250&oauth_token={}&v=20131026&offset={}'

token = secret.TOKEN # replace with oauth token
offset = 0
data = []
 
with open("checkins.json", 'w') as f:
    while True:
        response = requests.get(url_template.format(token, offset))
        if len(response.json()['response']['checkins']['items']) == 0:
            break
 
        data.append(response.json())
        offset += 250
            
    f.write(json.dumps(data))