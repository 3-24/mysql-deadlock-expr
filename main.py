import subprocess as sp
import mysql.connector
import sys

n = int(sys.argv[1])

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  port=3306,
  database="deadlock",
  password="password",
  autocommit=False
)


c = conn.cursor()

c.execute("DROP TABLE t;")
c.execute("CREATE TABLE t (i INT PRIMARY KEY, j INT) Engine=InnoDB;")

for i in range (n):
    c.execute("INSERT INTO t (i, j) VALUES (%s, %s)", (i, 0))

conn.commit()
conn.close()

command = " & ".join(map(lambda i: f"python3.10 expr.py {i} {n}" , range(n)))
# print(command)
sp.run(command, shell=True)
