import psycopg2
conn1=psycopg2.connect(user="postgres",
                            password="GURUG",
                            host="127.0.0.1",
                            port="5432",
                            database="MYDB1")
cur1 = connection.cursor()
