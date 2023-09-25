#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# UPDEL_MY.py

"""
  Nesse arquivo, vamos 
  fazer um teste de
  update e delete ao banco 
  de dados do MySQL.

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
	cur.execute("update cliente set nome='Alberto' where id=1")
	print "Atualização feita com sucesso"
	cur.execute("delete from cliente where id=2")
	con.commit()
	print "Registro apagado com sucesso"
except Exception as e:
	print "Erro: %s"%e
	con.rollback
finally:
	print "Finalizando a conexão com o banco de dados"
	cur.close()
	con.close()


