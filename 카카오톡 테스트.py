import requests
import json





###################### 카카오톡으로 보내기 소스######################################
        

with open(r"C:\Users\JSJ\week4\week4\kakao_code.json","r") as fp:
    tokens = json.load(fp)
# print(tokens)
# print(tokens["access_token"])

friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

# GET /v1/api/talk/friends HTTP/1.1
# Host: kapi.kakao.com
# Authorization: Bearer {ACCESS_TOKEN}

headers={"Authorization" : "Bearer " + tokens["access_token"]}

result = json.loads(requests.get(friend_url, headers=headers).text)

print(type(result))
print("=============================================")
print(result)
print("=============================================")
friends_list = result.get("elements")
for fda in range(2):
    print(friends_list[fda])
    # print(type(friends_list))
    print("=============================================")
    print(friends_list[fda].get("uuid"))
    friend_id = friends_list[fda].get("uuid")
    print(friend_id)
    
    send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
    
    data={
        'receiver_uuids': '["{}"]'.format(friend_id),
        "template_object": json.dumps({
            "object_type":"text",
            "text":"진짜로 되는거야? 이제!!!!!!",
            "link":{
                "web_url":"www.daum.net",
                "web_url":"www.naver.com"
            },
            "button_title": "바로 확인"
        })
    }
    
    response = requests.post(send_url, headers=headers, data=data)
    response.status_code
    






    