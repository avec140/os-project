import pymysql 

conn = pymysql.connect(host='localhost', user='root', password='1234', db='developer', charset='utf8') 


cursor = conn.cursor() 

sql = "SELECT * FROM news" 

cursor.execute(sql)

row = cursor.fetchall()
print(row)

conn.close()