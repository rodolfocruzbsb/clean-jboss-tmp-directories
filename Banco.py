#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#importando módulo do SQlite
import sqlite3

class Banco():

	def __init__(self):
	    self.conexao = sqlite3.connect('favorites.db')
	    self.createTable()

	def createTable(self):
	    c = self.conexao.cursor()

	    c.execute("""create table if not exists favorite_server (
	                   id integer primary key autoincrement ,
	                   default boolean not null,
	                   fullpath text)""")
	    self.conexao.commit()
	    c.close()