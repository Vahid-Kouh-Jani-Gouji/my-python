import mysql.connector as mysql
import pyodbc

server = "<localhost>,<6789>"
database = "<library>"
username = "<mysqluser>"
password = "<1234qwer>"
conn_str = f"Driver=SQL Server;Server={server};Database={database};UID={username};PWD={password}"
cnxn = pyodbc.connect(conn_str)

# Use the connection object to execute SQL queries and retrieve results

# db = mysql.connect(host="localhost",user="root", password ="vahid",database="library")

cursor= db.cursor()


#creat customers table
sql_creat_customers_table="CREATE TABLE IF NOT EXISTS customers (customer_id INT AUTO_INCREMENT PRIMARY KEY , name  VARCHAR(255) NOT NULL ,address  VARCHAR(255) NOT NULL)"
cursor.execute(sql_creat_customers_table)

#creat books table
sql_creat_books_table="CREATE TABLE IF NOT EXISTS books (ISDN INT PRIMARY KEY NOT NULL , name_book VARCHAR(255) NOT NULL,author VARCHAR(255) NOT NULL, title VARCHAR(255) NOT NULL ,customer_id int,is_active BIT(1) DEFAULT 0,CONSTRAINT chk_is_active CHECK(is_active IN (0,1)),foreign key(customer_id) references customers(customer_id)) "
cursor.execute(sql_creat_books_table)

#creat bookings table
sql_creat_bookings_table="CREATE TABLE IF NOT EXISTS bookings ( booking_id INT auto_increment primary KEY , booking_start date NOT NULL,booking_end date NOT NULL, booking_finish date NOT NULL ,ISDN int  ,customer_id int ,foreign key (ISDN) references books(ISDN),foreign key(customer_id) references customers(customer_id))"
cursor.execute(sql_creat_bookings_table)
# #insert values into customers table
# sql_insert_customer ="INSERT INTO customers (name,address) VALUES (%s,%s)"
# Valuues= ("ali","uhlandweg")
# cursor.execute(sql_insert_customer,Valuues)
# db.commit()

# #insert values into books table
# sql_insert_book ="INSERT INTO books (ISDN,name,author,title,is_active) VALUES (%d,%s,%s,%s,%d)"
# Valuues= (10,"dastan","nevisande","baghvahsh",1)
# cursor.execute(sql_insert_book,Valuues)
# db.commit()