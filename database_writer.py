import mysql.connector

mydb = mysql.connector.connect(
    host="10.9.71.238",
    user="petta",
    passwd="petta",
    database="pettadb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO testwriting (time, pressure) VALUES (%s, %s)"
val = ("John", "Highway 21")3
mycursor.execute(sql, val)

mydb.commit()