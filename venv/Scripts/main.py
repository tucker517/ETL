from sql_queries import

from ETL_MultiDB.py import ETL

def main():
    print('Starting ETL Processes...')

    # establish connection for target database (sql-server)
    target_cnx = pyodbc.connect(**datawarehouse_db_config)

    # loop through credentials for each db instance case
    # Mysql instance
    for config in mysql_db_config:
        try:
            print("Loading DB: " + config['database'])
            etl_process(mysql_queries, target_cnx, config, 'mysql')
        except Exception as error:
            print("etl for {} has error".format(config['database']))
            print('error message: {}'.format(error))
            continue

    # SQL Server Instance
    for config in sqlserver_db_config:
        try:
            print("Loading DB: " + config['database'])
            etl_process(sqlserver_queries, target_cnx, config, 'sqlserver')
        except Exception as e:
            print("ETL for {} has encountered an error".format(config['database']))
            print('error message: {}'.format(error))
            continue

    # Firebird Instance
    for config in fbd_db_config:
        try:
            print("Loading DB: " + config['database'])
            etl_process(fbd_queries, target_cnx, config, 'firebird')
        except Exception as error:
            print("ETL for {} encountered an error".format(config['database']))
            print('error message: {}'.format(error))
            continue

    target_cnx.close()


if __name__ == "__main__":
    main()