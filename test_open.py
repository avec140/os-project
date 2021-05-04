import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'e01e1d06626cb6e4b00771bd3584c765'
redirect_uri = 'http://example.com/oauth'
authorize_code = 'd9SRpQmadxX6WVjFGVpPSLEumMJAQMX5zoD4uQrCkieMAyA9EMmBKbVV9VH9A9Adg6Y_1Ao9dNkAAAF5NlSirg'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
#1.
with open(r"C:\Users\know9\Desktop\kakao_test\kakao_code.json","w") as fp:
    json.dump(tokens, fp)


#출처 : https://novice-engineers.tistory.com/9?category=908185
