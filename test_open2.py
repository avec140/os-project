import json
#1.
with open(r"C:\Users\know9\Desktop\kakao_test\kakao_code.json","r") as kakao:
     json_data = json.load(kakao)
    
# with open("kakao_code.json","w") as fp:
#    ts = json.load(fp)
    
print(json_data)
print(json_data["access_token"])


#출처 : https://novice-engineers.tistory.com/9?category=908185
