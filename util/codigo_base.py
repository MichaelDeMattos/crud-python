#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import os

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

ui = Gtk.Builder()
ui.add_from_file("teste.ui")

class Handler(object):

    def __init__(self, *args, **kwargs):
        super(Handler, self).__init__(*args, **kwargs)
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # -->  Variáveis globais

ui.connect_signals(Handler())
window = ui.get_object("jn_a")
window.show_all()

if __name__ == '__main__':
    Gtk.main()

