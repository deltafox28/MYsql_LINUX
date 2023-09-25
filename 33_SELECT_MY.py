#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# SELECT_MY.py

"""
  Nesse arquivo, vamos 
  fazer um teste de
  update e delete ao banco 
  de dados do MySQL.

  Modificado em 27 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""
import sys

try:
	import MySQLdb
except:
    sys.exit("[!] Por favor, intale a biblioteca mysqldb com o comando: sudo apt-get install python-mysqldb")

try:
	con = MySQLdb.connect(host="127.0.0.1", user="root", db="projeto", passwd="123456") 
	cur = con.cursor()
	cur.execute("select * from cliente")
	print "Primeiro registro: ",cur.fetchone()
	print "Todos os registros: ",cur.fetchall()
except Exception as e:
	print "Erro: %s"%e
	con.rollback # Rollback feito de propósito!
finally:
	print "Finalizando a conexão com o banco de dados"
	cur.close()
	con.close()









