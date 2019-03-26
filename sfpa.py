#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyfiglet import Figlet
from clint.textui import colored
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os, sys, platform, time, progressbar

class SeleniumFbAutomation:
	def __init__(self):
		firefox_options = Options()
		firefox_options.set_headless()
		self.browser = Firefox(options=firefox_options)
		self.browser = webdriver.Firefox()
		self.browser.get("https://mbasic.facebook.com/login")

	def autenticar(self, email, senha):
		self.browser.find_element_by_xpath("//input[@id='m_login_email' or @name='email']").send_keys(email)
		self.browser.find_element_by_xpath("//input[@name='pass']").send_keys(senha)
		self.browser.find_element_by_xpath("//input[@value='Entrar']").click()
		try:
			self.browser.find_element_by_xpath("//input[@value='OK']").click()
			print(self.tipo_mensagem("sucesso", u"Logado no Facebook."))
		except NoSuchElementException:
			print(self.tipo_mensagem("erro", u"O e-mail ou senha que você inseriu está incorreta."))
			self.browser.close()
			self.finalizar()

	def post_profile(self, postagem, imagem):
		self.browser.get("https://mbasic.facebook.com/profile.php")
		usuario = self.browser.title
		self.browser.find_element_by_xpath("//textarea[@name='xc_message']").send_keys(postagem)
		time.sleep(20)

		if os.path.exists(imagem):
			self.browser.find_element_by_xpath("//input[@value='Foto' or name='view_photo']").click()
			self.browser.find_element_by_xpath("//input[@name='file1']").send_keys(imagem)
			time.sleep(8)
			self.browser.find_element_by_xpath("//input[@value='Prévia' or name='add_photo_done']").click()
		else:
			print(self.tipo_mensagem("erro", u"Não foi possivel encontrar essa imagem."))
			self.browser.close()
			self.finalizar()

		try:
			time.sleep(8)
			self.browser.find_element_by_xpath("//input[@value='Publicar' or name='view_post']").click()
			print(self.tipo_mensagem("sucesso", u"Postado no perfil de "+usuario+"."))
		except NoSuchElementException:
			print(self.tipo_mensagem("erro", u"Não foi possivel postar no perfil de "+usuario+"."))
			self.browser.close()
			self.finalizar()

	def post_page(self, pagina, postagem, imagem):
		self.browser.get("https://mbasic.facebook.com/"+pagina+"/")
		nome_pagina = self.browser.title
		self.browser.find_element_by_xpath("//textarea[@name='xc_message']").send_keys(postagem)
		time.sleep(20)

		if os.path.exists(imagem):
			self.browser.find_element_by_xpath("//input[@value='Mais']").click()
			self.browser.find_element_by_xpath("//input[@value='Foto' or name='view_photo']").click()
			self.browser.find_element_by_xpath("//input[@name='file1']").send_keys(imagem)
			time.sleep(8)
			self.browser.find_element_by_xpath("//input[@value='Prévia' or name='add_photo_done']").click()
		else:
			print(self.tipo_mensagem("erro", u"Não foi possivel encontrar essa imagem."))
			self.browser.close()
			self.finalizar()

		try:
			time.sleep(8)
			self.browser.find_element_by_xpath("//input[@value='Publicar' or name='view_post']").click()
			print(self.tipo_mensagem("sucesso", u"Postado no página de "+nome_pagina+"."))
		except NoSuchElementException:
			print(self.tipo_mensagem("erro", u"Não foi possivel postar no página de "+nome_pagina+"."))
			self.browser.close()
			self.finalizar()

	def post_group(self, grupo, postagem, imagem):
		self.browser.get("https://mbasic.facebook.com/groups/"+grupo+"/")
		nome_grupo = self.browser.title

		try:
			self.browser.find_element_by_xpath(u"//input[@value='Participar do grupo']").click()
			print(self.tipo_mensagem("alerta", u"Solicitação de participar no grupo "+nome_grupo+" foi enviada."))
		except NoSuchElementException:
			try:
				self.browser.find_element_by_xpath(u"//input[@value='Cancelar solicitação de participação']")
				print(self.tipo_mensagem("alerta", u"Solicitação de participar no grupo "+nome_grupo+u" está em análise."))
			except NoSuchElementException:
				try:
					self.browser.find_element_by_xpath("//textarea[@name='xc_message']").send_keys(postagem)
					time.sleep(20)

					if os.path.exists(imagem):
						self.browser.find_element_by_xpath("//input[@value='Foto' or name='view_photo']").click()
						self.browser.find_element_by_xpath("//input[@name='file1']").send_keys(imagem)
						time.sleep(12)
						self.browser.find_element_by_xpath("//input[@value='Prévia' or name='add_photo_done']").click()
					else:
						print(self.tipo_mensagem("erro", u"Não foi possivel encontrar essa imagem."))
						self.browser.close()
						self.finalizar()

					try:
						time.sleep(10)
						self.browser.find_element_by_xpath("//input[@value='Publicar' or name='view_post']").click()
						print(self.tipo_mensagem("sucesso", u"Postado no grupo "+nome_grupo+"."))
						self.progress_bar(0.90)
					except NoSuchElementException:
						print(self.tipo_mensagem("erro", u"Não foi possivel postar no grupo "+nome_grupo+"."))
						self.browser.close()
						self.finalizar()
				except NoSuchElementException:
					pass


	def requests_group(self, grupo):
		self.browser.get("https://mbasic.facebook.com/groups/"+grupo+"/madminpanel/requests/")
		
		try:
			time.sleep(10)
			self.browser.find_element_by_xpath("//input[@value='Aprovar tudo' or name='approve_all']").click()
			print(self.tipo_mensagem("sucesso", u"Aprovado todas as solicitações de entrada no grupo."))
			time.sleep(10)
		except NoSuchElementException:
			pass


	def post_birthday(self, postagem, imagem):
		self.browser.get("https://mbasic.facebook.com/events/calendar/birthdays/")

		try:
			print(self.tipo_mensagem("sucesso", u"Postado a parabenização de '+contato+'."))
		except NoSuchElementException:
			print(self.tipo_mensagem("erro", u"Não foi possivel postar parabenização de '+contato+'."))
			self.browser.close()
			self.finalizar()

	def tipo_mensagem(self, tipo, mensagem):
		if tipo == "sucesso":
			return colored.green("[+] Sucesso: "+mensagem)
		elif tipo == "alerta":
			return colored.yellow("[!] Alerta: "+mensagem)
		elif tipo == "erro":
			return colored.red("[-] Erro: "+mensagem)

	def progress_bar(self, tempo):
		widgets = ['Proxima postagem ', progressbar.Bar(),' (', progressbar.ETA(), ') ']
		for i in progressbar.progressbar(range(100), widgets=widgets):
		    time.sleep(tempo)

	def sistema_operacional(self):
	    if platform.system() == "Windows":
	         return True
	    else:
	         return False

	def qual_turno(self):
	    hora = datetime.now().strftime("%H")
	    if hora >= "06" and hora <= "11":
	    	return True
	    elif hora >= "11" and hora <= "18":
	    	return False
	    else:
	    	return False

	def limpar_terminal(self):
		if self.sistema_operacional():
			os.system("cls")
		else:
			os.system("clear")

	def finalizar(self):
		self.browser.quit()
		print(self.tipo_mensagem("sucesso", u"Script foi finalizado."))

	def remove_repetidos(self, lista):
	    nova_lista = []
	    for i in lista:
	        if i not in nova_lista:
	            nova_lista.append(i)
	    nova_lista.sort()
	    return nova_lista

	def show_graph(self):
		Graph = Figlet(font="slant")
		GraphRender = Graph.renderText("FacebookBot")
		self.limpar_terminal()
		print("%s" % (colored.cyan(GraphRender)))
		print(colored.cyan("Automatização de postagens para Facebook.\nNão me responsabilizo por possíveis Bloqueios e pedidos de troca de senha.\nBy Nícolas Pastorello (https://github.com/nicopastorello)\n"))
