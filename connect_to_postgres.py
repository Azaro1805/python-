import psycopg2
import psycopg2.extras


DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "admin"


#conn = connection, here i create the connection to the pgadmin DB
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST ) 

# in cursor i will execute all the functions like sql query and need to close it after finish
cur = conn.cursor() 


#cursor which return dictiory insted of tuples
#cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 

# option 1:  
# the diff is the after the cur is over we not need to close/commit him. its close and commit  automaticly. not need to write cur.close() and conn.close() and conn.commit() 

with conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM student;")
        print(cur.fetchall()) 




# option 2:  

'''

#-------------------------------- SQL Querys-------------------------------------------

#cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")

#cur.execute("INSERT INTO student (name) VALUES(%s)", ("Antony",))

cur.execute("SELECT * FROM student;")

# to view the execute we use fetchall
print(cur.fetchall()) 

cur.execute("SELECT * FROM student WHERE id = %s;" , (1,))

# to view the execute of only one student we use fetchone 
print(cur.fetchone())


#--------------------------------End SQL Querys-------------------------------------------
# save anything that i run 
conn.commit() 

cur.close()

conn.close()

'''



