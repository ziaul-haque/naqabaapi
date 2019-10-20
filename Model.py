import pyodbc
import redis
from logger import logger

driver = '{SQL Server}'
# driver = '{ODBC Driver 17 for SQL Server}'
server = '119.42.57.238'
database = 'daif-avl-db'
username = 'sa'
password = 'Naqaba@password01'
conn_string = 'Driver=' + driver + ';Server=' + server + ';Database=' + database + ';UID=' + username + ';PWD=' + password
db_con = pyodbc.connect(conn_string)

cursor = db_con.cursor()

cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()
try:
    cache_db = redis.StrictRedis(host="localhost", port=6379, db=0)
    logger.info("redis cache server connected")
except Exception as e:
    logger.error(e)




