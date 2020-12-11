#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import os
import sqlite3
import datetime
from mikeUtil import MikeGtk

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

ui = Gtk.Builder()
ui.add_from_file("interface.ui")

class Handler(MikeGtk):

	def __init__(self, *args, **kwargs):
		super(Handler, self).__init__(*args, **kwargs)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# -->  Variáveis globais
		# Janela de Login
		self.jan_login = ui.get_object("jn_login")
		self.jan_login.show_all()
		self.entry_usuario = ui.get_object("entry_usuario")
		self.entry_senha = ui.get_object("entry_senha")
	
		# Message Dialog
		self.msg_box = ui.get_object("msg_box")
		
		# janela principal
		self.jn_principal = ui.get_object("jn_principal")
		
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# --> Fechar janela de login
	def ao_destruir_jn_login(self, *args):
		pass
		
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# --> Executa o login
	def ao_clicar_em_bt_login(self, *args):
		pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	#--> Chamar uma nova Janela no mesmo arquivo glade
	def new_window_main(self, new_window, now_window,  modal=False, 
						destroy_parent=False, maximize=False):
		new_window.set_transient_for(now_window)
		new_window.set_modal(modal)
		new_window.set_destroy_with_parent(destroy_parent)
		new_window.show_all()
		if maximize == True:
			new_window.maximize()
			
if __name__ == '__main__':
    ui.connect_signals(Handler())
    Gtk.main()
