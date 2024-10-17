import pyodbc
from util.DBpropertyutil import DbPropertyUtil

class DbConnUtil:
    @staticmethod
    def getConnection():
        connection_string = DbPropertyUtil.getConnectionString()
        conn = pyodbc.connect(connection_string)
        return conn
    