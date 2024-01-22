import pymysql
from pymysql.cursors import Cursor

conn = pymysql.connect(host='43.202.67.57', user='mysql', password='1234', db='test', charset='utf8', autocommit=True)
cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = "insert into tbl_member(email, password, name) values ('uj06134', '1234', '김훈종')"
# cursor.execute(sql)
# conn.commit()

sql = "select email, password, name from tbl_member"
cursor.execute(sql)

# fetchall(): 모든 결과 데이터를 가져올 때 사용
# fetchone(): 결과 중 첫 번째 데이터를 가져올 때 사용
# fetchmany(n): 결과 중 n개의 데이터를 가져올 때 사용
print(cursor.fetchall())
conn.commit()

cursor.close()
conn.close()