# SELECT, WHERE, FROM, LIKE, JOIN, MIN, MAX, ORDER BY, DESC, ON, DISTINCT
# SHOW TABLES
# CREATE DATABASE IF NOT EXISTS test_db
# CREATE TABLE IF NOT EXISTS name_table
# INSERT INTO name_table (columns, ...) VALUES (value, ...)
import sqlalchemy as db

meta = db.MetaData()

user = db.Table(
    'User', meta,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('login', db.String(150), nullable=False),
    db.Column('password', db.String(150), nullable=False)
)
print(user.c)

engine = db.create_engine('mysql+mysqlconnector://root:qwerty123@localhost:3306/test_sqlalchemy')
meta.create_all(engine)

connection = engine.connect()
# заполнение таблицы данными
add_query = user.insert().values(login='user1', password='password1')
connection.execute(add_query)
connection.commit()
select_all_query = db.select(user) # SELECT * FROM User
print(connection.execute(select_all_query).fetchall())

search_password = user.select().where(user.c.id == '2')
result = connection.execute(search_password)
print(result.fetchall())
# Удаление
delete_query_with_id2 = user.delete().where(user.c.id == '2')
result = connection.execute(delete_query_with_id2)
connection.commit()
select_all_query = db.select(user) # SELECT * FROM User
print(connection.execute(select_all_query).fetchall())
# Обновление
update_query_with_id1 = user.update().values(login='user1_after_update').where(user.c.id == '1')
connection.execute(update_query_with_id1)
connection.commit()
select_all_query = db.select(user) # SELECT * FROM User
print(connection.execute(select_all_query).fetchall())

# Cортировка
sort_query = db.select(user).order_by(user.c.id)
print(connection.execute(sort_query).fetchall())
desc_sort_query = db.select(user).order_by(user.c.id.desc())
print(connection.execute(desc_sort_query).fetchall())

connection.close()




