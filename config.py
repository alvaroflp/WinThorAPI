import cx_Oracle

# Configurações do banco de dados Oracle
dsn = cx_Oracle.makedsn("127.0.0.1", 1521, service_name="WINT")
user = "ALVARO"
password = "TESTE"

# Configuração JWT
JWT_SECRET_KEY = "w08xL5JeUP6LH2Q50tlALMt2nxUv7F1i"