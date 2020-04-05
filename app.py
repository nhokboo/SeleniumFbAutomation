#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sfpa import SeleniumFbAutomation
import random

sfpa = SeleniumFbAutomation()

email 	= ''
senha 	= ''

postagem 	  = '👉 Pastorello - Assistência Técnica 👈\n🏅 Assistência Técnica Especializada\n📱 Fone: (54) 99701-9164.\n\n🚗 End: R. Marcos Nardon n° 69 - Fenavinho, Bento Gonçalves.\n\n⌚ Horário de atendimento\nSegunda à Sexta:\n7:30h às 18:00h\nSábados:\n07:30h às 15:00h\n\n#técnico #assistência #técnica #assistênciatécnica #tecnologia #inovação #pastorello #agilidade #profissionalismo #assistencia #manutencao #computadores #notebooks #gamers #nvidia #geforce #intel #amd #ryzen #suporte #bentogoncalves #solucoes #tecnico #microsoldering #microsoldagem #microsolda #solda #conserto #repair #fix #reparacion'
pagina 		  = 'PastorelloAssistenciaTecnica'
lista_imagens = ['C:\\Users\\Nícolas Pastorello\\Desktop\\SeleniumFbAutomation-master\\imagens\\01.png','C:\\Users\\Nícolas Pastorello\\Desktop\\SeleniumFbAutomation-master\\imagens\\02.png','C:\\Users\\Nícolas Pastorello\\Desktop\\SeleniumFbAutomation-master\\imagens\\03.png','C:\\Users\\Nícolas Pastorello\\Desktop\\SeleniumFbAutomation-master\\imagens\\04.png','C:\\Users\\Nícolas Pastorello\\Desktop\\SeleniumFbAutomation-master\\imagens\\05.png','C:\\Users\\Nícolas Pastorello\\Desktop\\SeleniumFbAutomation-master\\imagens\\06.png','C:\\Users\\Nícolas Pastorello\\Desktop\\SeleniumFbAutomation-master\\imagens\\07.png','C:\\Users\\Nícolas Pastorello\\Desktop\\SeleniumFbAutomation-master\\imagens\\08.png','C:\\Users\\Nícolas Pastorello\\Desktop\\SeleniumFbAutomation-master\\imagens\\09.png','C:\\Users\\Nícolas Pastorello\\Desktop\\SeleniumFbAutomation-master\\imagens\\10.png','C:\\Users\\Nícolas Pastorello\\Desktop\\SeleniumFbAutomation-master\\imagens\\11.png','C:\\Users\\Nícolas Pastorello\\Desktop\\SeleniumFbAutomation-master\\imagens\\11.png']
lista_grupos  = ['1459711954270466','343172739211759','1278058998946495','1586742354909212','294998417278124','307770416239580','469633646536045','258201714291546','750548974992961','692862957513901','1639117106331699','242063172564100','766877770001776','1552964371643764','121880017984824','549173861957708','1577366182564183','474713069317083','1523832431209344','725228584202844','621455297864848','749825018361273','383826408411478','996328937079195','492698777546546','259512470914251','393549894043627','395554883848795','524117857681736','1464159223841165','267100623476288','607140042631703','480707172034449','646742192132000','308046719319325','405616042818275','163604107139780','1383351131903410','275768365965477','505469092822522','293029710801257','522436421150725','718327341606318','607495159274855','1500074506917106','613777732097033','1630681840486594','424778297627014','650145621782175','1156621451019611','126654534210549','1185629608230877','276424769192493','1855023191451962','512638645425065','519131958150589','581288991887502','882235485125455','559401750830090','1554249051500372']

sfpa.show_graph()
sfpa.autenticar(email, senha)
sfpa.post_profile(postagem, random.choice(lista_imagens))
sfpa.progress_bar(2.40)
sfpa.post_page(pagina, postagem, random.choice(lista_imagens))
sfpa.progress_bar(3.60)

for id_group in lista_grupos:
	sfpa.requests_group(id_group)
	sfpa.post_group(id_group, postagem, random.choice(lista_imagens))
sfpa.finalizar()
