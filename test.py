import sqlite3
connection = sqlite3.connect('data.db')
cursor= connection.cursor()
create_table= "CREATE TABLE users (id int,username text, password text)"
cursor.execute(create_table)
user=(1,'bob','asdf')
insert_query="insert into users Values(?,?,?)"
cursor.execute(insert_query,user)
users = [
    (1,'timi','ybnl'),
    (3,'akin','yeri')
]
cursor.executemany(insert_query,users)
select_query= "select * from users"
for row in cursor.execute(select_query):
    print (row)
connection.commit()
connection.close
