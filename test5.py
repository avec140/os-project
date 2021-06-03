import requests
import json
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup


############################ 웹 크롤링 소스############################################
def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
second = sleeptime(0,0,6);
while 1==1:
    time.sleep(second);
    html=urlopen(
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%98").read().decode('utf-8')

    naver=BeautifulSoup(html,features='lxml')
    # text=naver.find('div',{'class','news_area'})
    text=naver.find_all('a',{'class','news_tit'}) 
    for m in text:
        print(m.attrs['href'])
        print(m.get_text())
        
        
#######################################################################################       



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
print(friends_list)
# print(type(friends_list))
print("=============================================")
print(friends_list[0].get("uuid"))
friend_id = friends_list[0].get("uuid")
print(friend_id)

send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

data={
    'receiver_uuids': '["{}"]'.format(friend_id),
    "template_object": json.dumps({
        "object_type":"text",
        "text":"print(m.attrs['href'])"
               "print(m.get_text())",
        "link":{
            "web_url":"www.daum.net",
            "web_url":"www.naver.com"
        },
        "button_title": "바로 확인"
    })
}

response = requests.post(send_url, headers=headers, data=data)
response.status_code







    