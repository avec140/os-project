import pymysql 

conn = pymysql.connect(host='localhost', user='root', password='1234', db='developer', charset='utf8') 

cursor = conn.cursor() 

sql = "INSERT INTO news (type, title_num, title, content) VALUES (%s, %s, %s, %s)" 

cursor.execute(sql,("news", "0607_1", "test_t_1", "contents_t_1")) 
cursor.execute(sql,("news","0607_2", "test_t_2", "contents_t_2")) 
cursor.execute(sql,("news","0607_3", "test_t_3", "contents_t_3")) 

conn.commit() 

conn.close() 
