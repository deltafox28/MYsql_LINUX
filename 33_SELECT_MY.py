#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# SELECT_MY.py

"""
  Nesse arquivo, vamos fazer um teste de consulta 
  ao banco de dados MySQL.
"""

import sys
import mysql.connector

try:
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        database="projeto",
        password="123456"
    )
    cur = con.cursor()

    # Executar a consulta SQL
    cur.execute("SELECT * FROM cliente")

    # Recuperar o primeiro registro
    first_record = cur.fetchone()
    print("Primeiro registro:", first_record)

    # Recuperar todos os registros restantes
    all_records = cur.fetchall()
    print("Todos os registros:", all_records)

except mysql.connector.Error as e:
    print("Erro:", e)
    con.rollback()  # Rollback em caso de erro

finally:
    print("Finalizando a conexão com o banco de dados")
    if con.is_connected():
        cur.close()
        con.close()









