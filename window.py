import sys
import os
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gtk

class mainWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title = "Hardening Script")
        
        
        
        self.button = Gtk.Button(label="test lmao")
        self.button.connect("clicked", self.button_clicked)
        self.add(self.button)
        self.set_default_size(1000,800)
        
    def button_clicked(self, widget):
        os.system("./testScript.sh")
window = mainWindow()


window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()