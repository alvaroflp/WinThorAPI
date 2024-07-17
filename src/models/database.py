import cx_Oracle
from config import dsn, user, password

class Database:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)
            print("Conectado ao banco de dados com sucesso.")
        except cx_Oracle.Error as error:
            print(f"Erro ao conectar ao banco de dados: {error}")
            self.connection = None

    def query(self, sql, params):
        if self.connection is None:
            raise Exception("Não conectado ao banco de dados.")
        cursor = self.connection.cursor()
        cursor.execute(sql, params)
        result = cursor.fetchall()
        cursor.close()
        return result

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexão com o banco de dados encerrada.")
