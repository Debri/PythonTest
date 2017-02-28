import pymysql



class MySQLCommand(object):
    def __init__(self, host, port, passwd, user, db, table):
        self.host = host
        self.passwd = passwd
        self.port = port
        self.db = db
        self.user = user
        self.table = table

    def conn_MySQL(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db,
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def query_MySQL(self):
        sql = 'SELECT * FROM account'
        result = self.cursor.execute(sql)
        print(result)
        for raw in self.cursor:
            print(raw)
        # for raw in result:
        #     print(raw)
        row = self.cursor.fetchone()
        print(row)

    def update_MySQL(self):
        sql = 'UPDATE account SET type="121" WHERE account_id=2'
        self.cursor.execute(sql)
        self.conn.commit()

    def add_MySQL(self):
        sql = 'INSERT INTO account (account_id,type,name) VALUES (4,4,"5")'
        self.cursor.execute(sql)
        self.conn.commit()

    def del_MySQL(self):
        sql = 'DELETE FROM account WHERE account_id=3'
        self.cursor.execute(sql)
        self.conn.commit()

    def close_conn_MySQL(self):
        self.cursor.close()
        self.conn.close()


exe = MySQLCommand(host="127.0.0.1", port=3306, user='root', passwd='123', db='exam', table='account')
exe.conn_MySQL()
# exe.add_MySQL()
exe.del_MySQL()
exe.query_MySQL()
# exe.cursor.commit()
exe.close_conn_MySQL()
# exe.update_MySQL()
