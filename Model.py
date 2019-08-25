import pyodbc
driver = '{SQL Server}'
# driver = '{ODBC Driver 17 for SQL Server}'
server = 'ec2-18-191-218-21.us-east-2.compute.amazonaws.com'
database = 'daif-avl-db'
username = 'sa'
password = 'Naqaba@password01'
conn_string = 'Driver=' + driver + ';Server=' + server + ';Database=' + database + ';UID=' + username + ';PWD=' + password
db_con = pyodbc.connect(conn_string)








