import psycopg2
from psycopg2.extensions import  ISOLATION_LEVEL_AUTOCOMMIT
import sys
import io
con_remote = psycopg2.connect(host="185.239.106.39", port=5432, user="test", password="12345",database="lab")
con_local=psycopg2.connect(host="localhost", port="5432",user="postgres",password="password")
con_local.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
con_remote.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
cur_remote = con_remote.cursor()
cur_local=con_local.cursor()
# cur_local.execute("CREATE DATABASE lab_local")
# cur_local.execute("CREATE TABLE person (id serial PRIMARY KEY, role_id integer, national_code char(10),birth_date date,first_name char(100),last_name char(100),password char(30), mobile char(11))")
# cur_local.execute("CREATE TABLE report (id serial , role_id integer, national_code char(10),birth_date date,first_name char(100),last_name char(100),password char(30), mobile char(11), name char(100))")







cur_local.close()
cur_remote.close()
# input = io.StringIO()
# cur.copy_expert('COPY (select * from person) TO STDOUT', input)
# input.seek(0)
# cur.copy_expert('COPY Orders2 FROM STDOUT', input)
# con.commit()