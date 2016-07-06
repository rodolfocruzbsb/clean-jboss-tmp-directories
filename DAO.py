#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from Banco import Banco
import os
import shutil
import datetime

   
class ServidoresDAO(object):


	def __init__(self, id = 0, default = 0, fullpath = ""):
		self.info = {}
		self.id = id
		self.default = default
		self.fullpath = fullpath

	def returnMessageSucesso(self, operacao):
		return operacao + " limpos com sucesso em "+datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

	######################### OPERACOES COM ARQUIVO #########################

	def removeArquivo(self, diretorioParaExcluir):
		##REMOVE O DIRETORIO
		shutil.rmtree(diretorioParaExcluir)

		##RECRIA O DIRETORIO
		os.mkdir(diretorioParaExcluir)
		
		##PERMISSIONS
		os.chmod(diretorioParaExcluir, 0777)##Read, write, and execute by owner, group, others.					

	def checkNotNull(self):
		if self.fullpath == "":
			raise ValueError("Path é Obrigatório!")

	def clearDeploys(self):
		try:
			self.checkNotNull()

			print("Removendo arquivos do Diretorio: "+self.fullpath + str("/standalone/deployments"))
			
			##os.rmdir(self.fullpath + str("/standalone/deployments/"))
			
			toremove = self.fullpath + str("/standalone/deployments")

			self.removeArquivo(toremove)
			
			return self.returnMessageSucesso("Deploys")
		except Exception,e: 
			print str(e)
			return "Erro ao limpar Deploys \n"+str(e)	

	def clearTmps(self):
		try:
			self.checkNotNull()

			print("Removendo arquivos do Diretorio: "+self.fullpath + str("/standalone/tmp"))						

			toremove = self.fullpath + str("/standalone/tmp")

			self.removeArquivo(toremove)

			return self.returnMessageSucesso("Temporários")
		except Exception,e: 
			print str(e)
			return "Erro ao limpar Temporários \n"+str(e)

	def clearLogs(self):
		try:
			self.checkNotNull()

			print("Removendo arquivos do Diretorio: "+self.fullpath + str("/standalone/log"))			
			
			toremove = self.fullpath + str("/standalone/log")

			self.removeArquivo(toremove)

			return self.returnMessageSucesso("Logs")
		except Exception,e: 
			print str(e)
			return "Erro ao limpar Logs \n"+str(e)


	######################### OPERACOES COM BANCO DE DADOS SQLITE #########################

	def insert(self):

		banco = Banco()
		try:

			c = banco.conexao.cursor()

			c.execute("insert into favorite_server (fullpath, default) values ('" + self.fullpath + ", 0' )")

			banco.conexao.commit()

			c.close()

			return "Servidor cadastrado com sucesso em "+datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		except Exception,e: 
			print str(e)
			return "Ocorreu um erro na inserção deste servidor"

	def insertDefault(self):

		banco = Banco()
		try:

			c = banco.conexao.cursor()

			c.execute("insert into favorite_server (fullpath, default) values ('" + self.fullpath + ", 1' )")

			banco.conexao.commit()

			c.close()

			return "Servidor cadastrado com sucesso em "+datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		except Exception,e: 
			print str(e)
			return "Ocorreu um erro na inserção deste servidor"

	def update(self):

		banco = Banco()
		try:

			c = banco.conexao.cursor()

			c.execute("update favorite_server set fullpath = '" + self.fullpath + "' where id = " + self.id + " ")

			banco.conexao.commit()

			c.close()

			return "Servidor atualizado com sucesso em "+datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		except Exception,e: 
			print str(e)
			return "Ocorreu um erro na alteração do servidor"

	def delete(self):

		banco = Banco()
		try:

			c = banco.conexao.cursor()

			c.execute("delete from favorite_server where id = " + self.id + " ")

			banco.conexao.commit()

			c.close()

			return "Servidor excluído com sucesso em "+datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		except Exception,e: 
			print str(e)
			return "Ocorreu um erro na exclusão do Servidor"

	def selectById(self, id):
		if id == "":
			return "Informe um ID para realizar a busca" 
			
		banco = Banco()
		try:

			c = banco.conexao.cursor()

			c.execute("select id, default, fullpath from favorite_server where id = " + id + "  ")

			for linha in c:
				self.id = linha[0]          
				self.default = linha[1]
				self.fullpath = linha[2]

			c.close()

			return "Busca feita com sucesso em "+datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		except Exception,e: 
			print str(e)
			return "Ocorreu um erro na busca do Servidor"