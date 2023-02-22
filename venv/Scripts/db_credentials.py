from variables.py import datawarehouse_name
# SQL Sever Target Database (datawarehouse)
datawarehouse_db_config = {
  'Trusted_Connection': 'yes',
  'driver': '{SQL Server}',
  'server': 'NITROHPC\SQLEXPRESS',
  'database': '{}'.format(datawarehouse_name),
  'user': 'Tucker',
  'password': 'Happy2020!!',
  'autocommit': True,
}

# SQL SERVER Source Database Credentials
sqlserver_db_config = [
  {
    'Trusted_Connection': 'yes',
    'driver': '{SQL Server}',
    'server': 'your_sql_server',
    'database': 'db1',
    'user': 'your_db_username',
    'password': 'your_db_password',
    'autocommit': True,
  }
]

# Mysql Source Database Credentials
mysql_db_config = [
  {
    'user': 'your_user_1',
    'password': 'your_password_1',
    'host': 'db_connection_string_1',
    'database': 'db_1',
  },
  {
    'user': 'your_user_2',
    'password': 'your_password_2',
    'host': 'db_connection_string_2',
    'database': 'db_2',
  },
]

# Firebird Source Database Credentials
fdb_db_config = [
  {
    'dsn': "/your/path/to/source.db",
    'user': "your_username",
    'password': "your_password",
  }
]
