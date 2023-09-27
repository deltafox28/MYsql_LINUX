#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# UPDEL_MY.py

"""
  Nesse arquivo, vamos fazer um teste de
  atualização e exclusão no banco de dados MySQL.
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

    # Atualização (UPDATE)
    cur.execute("UPDATE cliente SET nome='Alberto' WHERE id=1")
    con.commit()  # Commit após a atualização
    print("Atualização feita com sucesso")

    # Exclusão (DELETE)
    cur.execute("DELETE FROM cliente WHERE id=2")
    con.commit()  # Commit após a exclusão
    print("Registro apagado com sucesso")

except mysql.connector.Error as e:
    print("Erro:", e)
    con.rollback()  # Rollback em caso de erro

finally:
    print("Finalizando a conexão com o banco de dados")
    if con.is_connected():
        cur.close()
        con.close()


