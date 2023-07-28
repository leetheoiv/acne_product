from skincare_db import SQL

"""Create an instance of the SQL class"""
sql = SQL()

"""Create a table for skincare database"""
# sql.Query("""CREATE TABLE Product (productID int PRIMARY KEY AUTO_INCREMENT
#           ,brand VARCHAR(50),
#           procut_name VARCHAR(255),
#           type VARCHAR(50),
#           brand_link VARCHAR(255),
#           product_link VARCHAR(255),
#           price int,
#           MSRP int,
#           score float)""")



sql.insert_values("Product","brand",'Walmart,new_name,mositure,')

sql.show_table_values('SELECT * FROM Product')