import sqlite3

#Get a cursor
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()


#Part 1 - Making and populating a Database

create_table = """ 
CREATE TABLE  demo (
    s varchar(10),
    x int,
    y int
);"""

curs.execute(create_table)

conn.commit()

# Write INSERT INTO statements
curs.execute("""
INSERT INTO demo(
    s,x,y) VALUES("'g'", 3, 9)
    ;""")


curs.execute("""
INSERT INTO demo(
    s,x,y) VALUES("'v'", 5, 7)
    ;""")

curs.execute("""
INSERT INTO demo(
    s,x,y) VALUES("'f'", 8, 7)
    ;""")

conn.commit()

# Count how many rows you have
row_count = """SELECT COUNT(*)
FROM demo;"""

# How many rows are there where both x and y are >= 5
at_least_five = """SELECT COUNT(*)
FROM demo
WHERE demo.x >= 5 AND demo.y >= 5;"""


# How many unique values of y are there
unique_y = """ SELECT COUNT(DISTINCT(demo.y))
FROM demo;"""

def part_one(x):
    print(curs.execute(x).fetchall())

# Part 2 - The Northwind Database

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Fetchall data
curs.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY
name;""").fetchall()

# Query to see schema behind the table
curs.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()

# Ten most expensive items per unit price with descending order
top_ten_query = """
SELECT prod.ProductName, prod.UnitPrice
FROM Product AS prod
ORDER BY prod.UnitPrice DESC
LIMIT 10;"""


'''
ProductName	UnitPrice
0	Côte de Blaye	263.50
1	Thüringer Rostbratwurst	123.79
2	Mishi Kobe Niku	97.00
3	Sir Rodney's Marmalade	81.00
4	Carnarvon Tigers	62.50
5	Raclette Courdavault	55.00
6	Manjimup Dried Apples	53.00
7	Tarte au sucre	49.30
8	Ipoh Coffee	46.00
9	Rössle Sauerkraut	45.60
'''

#What is the average age of an employee at the time of their hiring?
avg_age_query = """
SELECT AVG(HireDate - BirthDate) as avg_age
FROM Employee;"""


#Part 3 - Sailing the Northwind Seas

# What are the ten most expensive items (per unit price) in the
# database *and*their suppliers?
top_ten_and_suppliers = """
SELECT prod.ProductName, prod.UnitPrice, sup.CompanyName
FROM Product AS prod
JOIN Supplier AS sup ON sup.ID = prod.SupplierID
ORDER BY prod.UnitPrice DESC
LIMIT 10;"""


# What is the largest category (by number of products in it)?
largest_category_query = """
SELECCT cat.CategoryName, COUNT(prod.CategoryID)
FROM Product AS prod
INNER JOIN Category AS cat
ON prod.CategoryID = cat.ID
GROUP BY prod.CategoryID
ORDER BY COUNT(prod.CategoryID) DESC
LIMIT 1;"""


'''
CategoryName  COUNT(prod.CategoryID)
0  Confections                      13 
'''

# (*Stretch*) What is the top territory (by number of employees),
# andhow many employees does it have?
# top_territory_query = """
# SELECT Territory.TerritoryDescription, COUNT()
# FROM EmployeeTerritory as et
# JOIN
# GROUP BY
# ORDER BY
# LIMIT 1;"""

def part_three(x):
    print(curs.execute(x).fetchall())