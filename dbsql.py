import mysql.connector.python
mydb = mysql.connector.connect(
  host="localhost",
  user="sayur_user",
  password="sayur!23",
  database="sayur_db"
)


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Fruit_Details (fruit_id INTEGER, name VARCHAR(255), color VARCHAR(255), cost DECIMAL(5,2), city VARCHAR(255))")

mycursor.execute("CREATE TABLE Fruit_Inventory(fruit_id INTEGER, quantity INTEGER, min_inventory INTEGER, reorder_qty INTEGER )")
mycursor.execute("SELECT  \
                    Fruit_Details.name, \
                    Fruit_Details.color, \
                    Fruit_Inventory.quantity \
                    FROM  Fruit_Details INNER JOIN Fruit_Inventory \
                    ON Fruit_Details.fruit_id = Fruit_Inventory.fruit_id")


myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mydb.commit()

mycursor.execute("INSERT INTO Fruit_Inventory VALUES (1, 100, 20, 20 )");
mycursor.execute("INSERT INTO Fruit_Inventory VALUES (2, 200, 10, 10)" );
mycursor.execute("INSERT INTO Fruit_Inventory VALUES (3, 50, 5, 5)");

mydb.commit()



