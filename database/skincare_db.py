import mysql.connector
from mysql.connector import Error





class SQL:
    def __init__(self):
        """Establish a connection to the database server"""
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="poohhouse24",
            database="skincare_db"
        )
        """Create a Cursor to interact with SQL server"""
        self.mycursor = self.db.cursor()

    """ Provides SQL Queries as desired"""
    def Query(self, query,):
        query = query
        return self.mycursor.execute(query)

    """Prints the values of a give table"""
    def show_table(self,table):
        self.mycursor.execute(f"DESCRIBE {table}")
        for x in self.mycursor:
            print(x)
    """Inserts values into a given table and desired column"""
    def insert_values(self,table_name,columns,values):
        return self.mycursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES (%s)",(values,))

    """Shows values of a table"""
    def show_table_values(self,command):
        self.mycursor.execute(command)
        for x in self.mycursor:
            print(x)

    """Commits the changes and saves them to the database"""
    def commit(self):
        self.db.commit()

    def close_connection(self):
        """Close the database connection"""
        self.mycursor.close()
        self.db.close()



