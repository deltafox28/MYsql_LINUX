import mysql.connector

try:
    # Conecta ao banco de dados
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="teste"
    )

    if connection.is_connected():
        print("Conexão ao MySQL bem-sucedida")

    # Execute suas consultas e operações aqui

except mysql.connector.Error as error:
    print("Erro ao conectar-se ao MySQL: {}".format(error))

finally:
    # Feche a conexão quando terminar
    if connection.is_connected():
        connection.close()
        print("Conexão ao MySQL fechada")
