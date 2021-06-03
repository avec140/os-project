import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'da8fa524d1039b99edd7f4f8a06ba2f5'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'U5pEx-1pZOnoE77f-NeqbnRHAU8a9vnQchoN6Ey1eUFzX7qvfLeLxrzRHx_E3Q8uJ7-0VwopyWAAAAF50BjGmQ'

       #카카오톡api 자체만의 응답캐시가 있어서 10분정도 기다림이 있어야한다.
      
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
with open(r"C:\Users\JSJ\week4\week4\kakao_code.json","w") as fp:
    json.dump(tokens, fp)