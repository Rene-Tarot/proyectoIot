import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="proyectoIot"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Responses (id INTEGER AUTO_INCREMENT PRIMARY KEY, tiempo TEXT, tiempoRes TEXT, nameOrigen VARCHAR(50), nameDestino VARCHAR(50), originIP VARCHAR(60), destIP VARCHAR(60), command VARCHAR(15), request VARCHAR(200), response VARCHAR(1024))")