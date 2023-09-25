#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# CON_MY.py

"""
  Nesse arquivo, vamos fazer um teste de
  conexão ao banco de dados 
  do MySQL.


  Modificado em 27 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

try:
	import MySQLdb
except:
    sys.exit("[!] Por favor, intale a biblioteca mysqldb com o comando: sudo apt-get install python-mysqldb")

try:
	con = MySQLdb.connect(host="127.0.0.1", user="root", db="projeto", passwd="123456") 
	cur = con.cursor()
	print "Feita a conexão com o banco de dados"

except Exception as e:
	print "Erro: %s"%e
finally:
	print "Finalizando a conexão com o banco de dados"
	cur.close()
	con.close()
