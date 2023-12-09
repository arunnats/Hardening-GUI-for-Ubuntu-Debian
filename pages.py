import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyApp(Gtk.Window):

    def __init__(self):
        super().__init__(title="Multi-page Application")
        self.set_default_size(1000, 800)

        # Create navigation bar
        self.navbar = Gtk.Box(spacing=10)
        self.back_button = Gtk.Button(label="Back")
        self.back_button.set_sensitive(False)
        self.back_button.connect("clicked", self.on_back_clicked)
        self.next_button = Gtk.Button(label="Next")
        self.next_button.connect("clicked", self.on_next_clicked)
        self.navbar.pack_start(self.back_button, False, True, 0)
        self.navbar.pack_end(self.next_button, False, True, 0)

        # Create stack for pages
        self.stack = Gtk.Stack()
        self.current_page = 1

        # Create page 1
        page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        label1 = Gtk.Label(label="Page 1")
        label1.set_halign(Gtk.Align.CENTER)
        confirm_button = Gtk.Button(label="Confirm")
        confirm_button.connect("clicked", self.on_confirm_clicked)
        page1.pack_start(label1, True, True, 0)
        page1.pack_start(confirm_button, True, True, 0)
        self.stack.add_named(page1, "page1")

        # Create page 2
        page2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        label2 = Gtk.Label(label="Page 2")
        label2.set_halign(Gtk.Align.CENTER)
        done_button = Gtk.Button(label="Done")
        done_button.connect("clicked", Gtk.main_quit)
        page2.pack_start(label2, True, True, 0)
        page2.pack_start(done_button, True, True, 0)
        self.stack.add_named(page2, "page2")

        # Add stack and navbar to window
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.pack_start(self.navbar, False, True, 0)
        vbox.pack_start(self.stack, True, True, 0)
        self.add(vbox)

        # Show initial page
        self.stack.set_visible_child_name(f"page{self.current_page}")

    def on_back_clicked(self, button):
        if self.current_page > 1:
            self.current_page -= 1
            self.stack.set_visible_child_name(f"page{self.current_page}")
            self.update_button_states()

    def on_next_clicked(self, button):
        if self.current_page < 2:
            self.current_page += 1
            self.stack.set_visible_child_name(f"page{self.current_page}")
            self.update_button_states()

    def on_confirm_clicked(self, button):
        self.current_page = 2
        self.stack.set_visible_child_name(f"page{self.current_page}")
        self.update_button_states()

    def update_button_states(self):
        self.back_button.set_sensitive(self.current_page > 1)
        self.next_button.set_sensitive(self.current_page < 2)

window = MyApp()
window.show_all()
Gtk.main()