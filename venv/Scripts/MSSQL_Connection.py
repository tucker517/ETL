import pyodbc
import pandas as pd
from sql_queries import SQLQuery


class MSSQL:
    # Initialize the common usable variables in below function:
    def __init__(self, username, password, server_name, db_name):
        self.username = username
        self.password = password
        self.server_name = server_name
        self.db_name = db_name
        self.uri = 'DRIVER={ODBC Driver 17 for SQL Server};' + self.server_name + ';DATABASE=' + self.db_name + ';UID=' + self.username + ';PWD=' + self.password
        try:
            self.client = pyodbc.connect(self.uri)
            self.db = self.client[self.db_name]
            print("MongoDB Connection Successful!")
        except Exception as e:
            print("Connection unsuccessful... Please try again...")
            print(e)

