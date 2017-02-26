import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123', db='exam', charset='UTF8')
cur = conn.cursor()
cur.execute("SELECT  acount()")
for i in cur:
    print(i)
cur.close()
conn.close()
