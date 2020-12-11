#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class MikeGtk(object):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#--> Simples MenssageBox/MessageDialog
	def simple_msg_box(self, component, title, text, icon=None):
		component.props.text = (title)
		component.props.secondary_text = (text)
		component.props.icon_name = (icon)
		component.show_all()
		component.run()
		component.hide()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#--> Estilos e Persolalização
	def style_app(self, style_path, set_screen):
		css_provider = Gtk.CssProvider()
		css_provider.load_from_path(style_path)
		style_context = Gtk.StyleContext()
		style_context.add_provider_for_screen(set_screen.get_default(),
                                              css_provider,
                                              Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
