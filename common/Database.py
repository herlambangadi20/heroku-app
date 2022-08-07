import psycopg2
from config import databaseConfig

class Database:
    def __init__(self):
        self.__connectDatabase()
    
    def __connectDatabase(self):
        """
            Fungsi ini digunakan untuk membuat koneksi awal ke Database,
            dengan konfigurasi yang diambil dari dict databaseConfig di
            file globalVar
        """
        self._conn = psycopg2.connect(
            host=databaseConfig['host'],
            port=databaseConfig['port'],
            dbname=databaseConfig['dbname'],
            user=databaseConfig['user'],
            password=databaseConfig['password'],
        )
        self._cur = self._conn.cursor()
       
    def executeQuery(self, query): 
        try:
            self._cur.execute(query)
            data = self._cur.fetchall()
            return data
        except psycopg2.Error as e:
            return e
    
    def executeQueryCommit(self, query): 
        try:
            self._cur.execute(query)
            data = self._cur.fetchall()
            self._conn.commit()
            return data
        except psycopg2.Error as e:
            return e
        
    def close(self):
        self._cur.close()
        self._conn.close()
        
class Connection():
    def __init__(self):
        self.conn=None

    def connect(self):
        self.conn=Database()
    
    def disconnect(self):
        del(self.conn)
    