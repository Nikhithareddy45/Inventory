import mysql.connector as m
conn=m.connect(host='localhost',username='root',password='Admin',database='inventory')
cur=conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Signup
    (user_id VARCHAR(10) PRIMARY KEY,
    First_name VARCHAR(50) NOT NULL,
    Email VARCHAR(100) ,
    Phone VARCHAR(20) ,
    UNIQUE (Email, Phone),
    Pass_word VARCHAR(100) NOT NULL,
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
cur.execute("""CREATE TABLE IF NOT EXISTS Stores
            (Store_id VARCHAR(10) PRIMARY KEY,
            Store_name VARCHAR(255) NOT NULL)""")
cur.execute("""CREATE TABLE IF NOT EXISTS User_Store(
            user_id VARCHAR(10),
            Store_id VARCHAR(10),
            PRIMARY KEY(user_id,store_id),
            FOREIGN KEY(user_id) REFERENCES Signup(user_id),
            FOREIGN KEY(Store_id) REFERENCES Stores(Store_id))""")
cur.execute("""CREATE TABLE IF NOT EXISTS Category
            (Categoryid VARCHAR(10) PRIMARY KEY,
            Category_name VARCHAR(255))""")
cur.execute("""CREATE TABLE IF NOT EXISTS Category_store
            (Categoryid VARCHAR(10),
            Store_id VARCHAR(10),
            PRIMARY KEY(Categoryid,Store_id),
            FOREIGN KEY(Categoryid) REFERENCES Category(Categoryid),
            FOREIGN KEY(Store_id) REFERENCES Stores(Store_id)) """)
cur.execute("""CREATE TABLE IF NOT EXISTS Item_store
            (Item_id VARCHAR(10) PRIMARY KEY,
            Item_name VARCHAR(255),
            Qty INT,
            Price INT NOT NULL,
            Units VARCHAR(50) NOT NULL,
            Dim1 VARCHAR(50),
            Dim2 VARCHAR(50),
            Categoryid VARCHAR(10),
            Store_id VARCHAR(10),
            UNIQUE(Item_id,Item_name,Qty,Price,Units,Dim1,Dim2,Categoryid,Store_id),
            FOREIGN KEY(Categoryid) REFERENCES Category(Categoryid),
            FOREIGN KEY(Store_id) REFERENCES Stores(Store_id))""")
cur.execute("""CREATE TABLE IF NOT EXISTS Cart(
            Cart_id VARCHAR(10) PRIMARY KEY,
            User_id VARCHAR(10),
            FOREIGN KEY(user_id) REFERENCES Signup(user_id))""")
cur.execute("""CREATE TABLE IF NOT EXISTS Cart_item(
            Cart_item_id VARCHAR(10) PRIMARY KEY,
            Cart_id VARCHAR(10),
            Item_id VARCHAR(10),
            FOREIGN KEY(Cart_id) REFERENCES Cart(Cart_id),
            FOREIGN KEY(Item_id) REFERENCES Item_store(Item_id),
            Qty VARCHAR(50)) """)
cur.execute("""CREATE TABLE IF NOT EXISTS Checkout(
            Checkout_id VARCHAR(10) PRIMARY KEY,
            user_id VARCHAR(10),
            FOREIGN KEY(user_id) REFERENCES Signup(user_id),
            Status VARCHAR(50),
            Total_price INT NOT NULL)""")
def insertion():
    cur.execute("SELECT COUNT(*) FROM Signup")
    row=cur.fetchone()
    if (row == 0):
        init=0
        first_value="{:04d}".format(init)
    else:
        init=row
        row+=1
        next_value="{:04d}".format(row)
