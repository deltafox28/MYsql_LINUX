#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# INSERT_MY.py

"""
  Nesse arquivo, vamos fazer um teste de
  conexão ao banco de dados 
  do MySQL.
"""

import sys
import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        database="teste",
        password="123456"
    )
    cur = con.cursor()
    cur.execute("INSERT INTO cliente(id, nome, cpf) VALUES (1, 'vitor', '333.333.222.55')")
    con.commit()  # Semelhante ao commit em outros bancos de dados
    print("Registro criado com sucesso")
except mysql.connector.Error as e:
    print("Erro:", e)
finally:
    print("Finalizando a conexão com o banco de dados")
    if con.is_connected():
        cur.close()
        con.close()
