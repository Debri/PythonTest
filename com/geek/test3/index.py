import pymysql


# py连接数据库
def conn_db():
    conn = pymysql.connect(host="127.0.0.1", user="root", password="123", db="exam", port=3306)
    cur = conn.cursor()
    return conn, cur


def exe_query(cur, sql):
    cur.execute(sql)
    return cur


conn, cur = conn_db()
cur = exe_query(cur, "SELECT * FROM account")
for itm in cur:
    print("ID=" + str(itm[0]))
cur.close()
conn.close()
