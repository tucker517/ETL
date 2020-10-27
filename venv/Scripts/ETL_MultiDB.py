'''
Author: Tucker Celestine
Class to perform Extraction, Transformation and Loading on data
from sources specfied in the queries file.
'''
import mysql.connector
import pyodbc
import fbd


class ETL:
    def __init__(self, query, source_cnx, target_cnx):
        # extract data from source db
        source_cursor = source_cnx.cursor()
        source_cursor.execute(query.extract_query)
        data = source_cursor.fetchall()
        source_cursor.close()

        # load data into warehouse db
        if data:
            target_cursor = target_cnx.cursor()
            target_cursor.execute("USE {}".format(datawarehouse_name))
            target_cursor.executemany(query.load_query, data)
            print('Data successfully loaded into datawarehouse!')
            target_cursor.close()
        else:
            print('Some error occured...')

    def etl_process(queries, target_cnx, source_db_config, db_platform):
        # establish source db connection
        if db_platform == 'mysql':
            source_cnx = mysql.connector.connect(**source_db_config)
        elif db_platform == 'sqlserver':
            source_cnx = pyodbc.connect(**source_db_config)
        elif db_platform == 'firebird':
            source_cnx = fdb.connect(**source_db_config)
        else:
            return 'ERROR! Unrecognized DataBase Platform!'

        # loop through sql queries
        for query in queries:
            etl(query, source_cnx, target_cnx)

        # close the source db connection
        source_cnx.close()