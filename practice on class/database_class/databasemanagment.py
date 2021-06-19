import psycopg2

conn = psycopg2.connect(host="185.239.106.39", port=5432, user="test", password="12345",
                        database="lab")

cursor = conn.cursor()

# cursor.execute("INSERT INTO test (name, description) VALUES ( 'sepekhrd', 'ahamditest')")
# conn.commit()
# cursor.execute("update test set name='corono4' where id=29")
# conn.commit()
cursor.execute("delete from test where id=29")
conn.commit()
cursor.close()
conn.close()
