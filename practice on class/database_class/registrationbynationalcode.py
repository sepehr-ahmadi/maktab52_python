import psycopg2
import datetime
import pprint

conn = psycopg2.connect(host="185.239.106.39", port=5432, user="test", password="12345",
                        database="lab")
cursor = conn.cursor()
requested_national_code = input("please enter national code:")
test_name=input("please enter test name:")

cursor.execute("select  * from  person where national_code=%s", (requested_national_code,))
conn.commit()
person_information_list = cursor.fetchone()
cursor.execute("select  * from  test where name=%s", (test_name,))
conn.commit()
test_information_list=cursor.fetchone()
print(test_information_list)
print(person_information_list)

cursor.execute("INSERT INTO test_answer (, description) VALUES ( 'sepekhrd', 'ahamditest')")
# conn.commit()
cursor.close()
conn.close()
