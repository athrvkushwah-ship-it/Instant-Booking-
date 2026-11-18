import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Wxyz@792",
    database="instant_boking"
)



cursor = db.cursor()
print("Connected to MySQL successfully!")

cursor.execute("SELECT moive_id,movie_name FROM movie ")
movie  = cursor.fetchall()

for movie  in movie :
    print(movie)
