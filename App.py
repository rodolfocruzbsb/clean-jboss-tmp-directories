#!/usr/local/bin/python
# -*- coding: utf-8 -*- 

from DAO import ServidoresDAO
from Tkinter import *
import ConfigParser
import os

class Application:
  def __init__(self, master=None):
      self.fonte = ("Verdana", "8")

      self.container1 = Frame(master)
      self.container1["pady"] = 10
      self.container1.pack()

      self.container2 = Frame(master)
      self.container2["padx"] = 10
      self.container2["pady"] = 5
      self.container2.pack()

      self.container3 = Frame(master)
      self.container3["padx"] = 20
      self.container3["pady"] = 5
      self.container3.pack()

      self.container4 = Frame(master)
      self.container4["pady"] = 15
      self.container4.pack()

      self.container5 = Frame(master)
      self.container5["pady"] = 15
      self.container5.pack()

      self.container6 = Frame(master)
      self.container6["pady"] = 15
      self.container6.pack()

      self.titulo = Label(self.container1, text="Informe os dados")
      self.titulo["font"] = ("Calibri", "9", "bold")
      self.titulo.pack ()

      self.lblpath = Label(self.container2, text="Path:", font=self.fonte, width=10)
      self.lblpath.pack(side=LEFT)

      self.txtpath = Entry(self.container2)
      self.txtpath["width"] = 40
      self.txtpath["font"] = self.fonte
      self.txtpath.pack(side=LEFT)

      self.btnLimpar = Button(self.container2, text="Limpar", font=self.fonte, width=10)
      self.btnLimpar["command"] = self.clear
      self.btnLimpar.pack(side=RIGHT)  

      self.tmp = BooleanVar()
      self.chkTmp = Checkbutton(self.container3, text="Tmp", variable=self.tmp)      
      self.chkTmp.pack (side=LEFT)  
      self.tmp.set(True) 

      self.log = BooleanVar()
      self.chkTmp = Checkbutton(self.container3, text="Log", variable=self.log)      
      self.chkTmp.pack (side=LEFT)  
      self.log.set(True)

      self.deploy = BooleanVar()
      self.chkTmp = Checkbutton(self.container3, text="Deploy", variable=self.deploy)      
      self.chkTmp.pack (side=LEFT)  
      self.deploy.set(True)


      self.lblmsgTmp = Label(self.container4, text="")
      self.lblmsgTmp["font"] = ("Verdana", "9", "italic")
      self.lblmsgTmp.pack()

      self.lblmsgLog = Label(self.container5, text="")
      self.lblmsgLog["font"] = ("Verdana", "9", "italic")
      self.lblmsgLog.pack()

      self.lblmsgDeploy = Label(self.container6, text="")
      self.lblmsgDeploy["font"] = ("Verdana", "9", "italic")
      self.lblmsgDeploy.pack()

      self.buscarPreferencial()

  ## Limpar diretorios do JBOSS
  def clear(self):

      dao = ServidoresDAO()

      dao.fullpath = self.txtpath.get()      

      ## TEMPORARIOS
      if self.tmp.get():            
            self.lblmsgTmp["text"] = dao.clearTmps() 
      else:
            self.lblmsgTmp["text"] = ""

      ## LOGS
      if self.log.get():            
            self.lblmsgLog["text"] = dao.clearLogs()
      else:
            self.lblmsgLog["text"] = ""

      ##DEPLOYS
      if self.deploy.get():            
            self.lblmsgDeploy["text"] = dao.clearDeploys()
      else:
            self.lblmsgDeploy["text"] = ""

  ## Inicia com diretorio configurado como DEFAULT no arquivo condig.ini
  def buscarPreferencial(self):      

      cfg = ConfigParser.ConfigParser() 
      
      cfg.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'conf', 'config.ini'))      
            
      pathDefault = cfg.get('dir', 'default')

      self.txtpath.delete(0, END)
      
      self.txtpath.insert(INSERT, pathDefault)



root = Tk()
root.wm_title("Clean JBoss - @RodolfoCruzTI")
Application(root)
root.mainloop()
