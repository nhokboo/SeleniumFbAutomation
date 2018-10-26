#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sfpa import SeleniumFbAutomation
import os, json, random, ConfigParser

config = ConfigParser.ConfigParser()
config.read(os.path.abspath('config.ini'))

sfpa = SeleniumFbAutomation()

if sfpa.qual_turno():
	email = config.get('Contas', 'email_1')
	senha = config.get('Contas', 'senha_1')
else:
	email = config.get('Contas', 'email_2')
	senha = config.get('Contas', 'senha_2')

postagem 		= config.get('Postagem', 'postagem')
lista_imagens 	= random.choice(json.loads(config.get('Postagem', 'imagens')))
pagina  		= config.get('Postagem', 'pagina')
lista_grupos 	= json.loads(config.get('Postagem', 'grupos'))

sfpa.show_graph()
sfpa.autenticar(email, senha)
sfpa.post_profile(postagem, lista_imagens)
sfpa.progress_bar(0.90)
sfpa.post_page(pagina , postagem, lista_imagens)
sfpa.progress_bar(0.90)

for id_group in sfpa.remove_repetidos(lista_grupos):
	sfpa.invite_group(id_group)
	sfpa.post_group(id_group, postagem, lista_imagens)
	sfpa.progress_bar(0.90)
sfpa.finalizar()