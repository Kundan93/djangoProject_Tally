import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="PKgon_d16",
  database="IRO"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM companies")

myresult = mycursor.fetchall()
print(myresult)