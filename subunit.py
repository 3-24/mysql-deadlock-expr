import mysql.connector
import sys
import time

n = int(sys.argv[2])
i = int(sys.argv[1])

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  port=3306,
  database="deadlock",
  password="password",
  autocommit=False
)


c = conn.cursor()
"""
c.execute("SELECT j FROM t WHERE i=%s FOR SHARE;", (i,))
c.fetchall()
time.sleep(5)
start = time.time()
try:
    c.execute("UPDATE t SET j=1 WHERE i=%s;", ((i+1) % n,))
except mysql.connector.errors.InternalError:
    end = time.time()
    spent = end - start
    #print(spent)
    with open("result.txt", "a") as f:
        f.write(f"{spent}\n")
"""

start = time.time()
c.execute("UPDATE t SET j=1 WHERE i=%s;", ((i+1) % n,))
end = time.time()
spent = end - start
with open("result.txt", "a") as f:
  f.write(f"{spent}\n")


conn.close()