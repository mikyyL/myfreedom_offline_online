import random

import mysql.connector as mysql

connection = mysql.connect(
    host='localhost',
    user='root',
    password='qwerty123',
    database='test_db'
)
cursor = connection.cursor()
cursor.execute("""CREATE DATABASE IF NOT EXISTS test_db""")
cursor.execute("""SHOW DATABASES""")
print(cursor.fetchall())
cursor.execute("""CREATE TABLE IF NOT EXISTS test_table (id INT AUTO_INCREMENT PRIMARY KEY, num1 INT(9), num2 INT(9))""")
cursor.execute("""SHOW TABLES""")
print(cursor.fetchall())
# cursor.execute("""INSERT INTO test_table (num1, num2) VALUES (1, 2);""")
# connection.commit()
# cursor.execute("""SELECT * FROM test_table;""")
# print(cursor.fetchall())
x = random.randint(1, 10)
y = random.randint(1, 10)
cursor.execute("""INSERT INTO test_table (num1, num2) VALUES (%s, %s);""", (x, y))
connection.commit()
cursor.execute("""SELECT * FROM test_table;""")
print(cursor.fetchall())
# Обновление
cursor.execute("""UPDATE test_table SET num1=65 WHERE id=4;""")
connection.commit()
cursor.execute("""SELECT * FROM test_table;""")
print(cursor.fetchall())
# Удаление
cursor.execute("""DELETE FROM test_table WHERE id=2;""")
connection.commit()
cursor.execute("""SELECT * FROM test_table;""")
print(cursor.fetchall())
