import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Operating System Hardening")
        self.set_default_size(1000, 800)
        self.set_border_width(10)

        # Create heading label using Pango markup
        heading_label = Gtk.Label()
        heading_label.set_markup("<big><b>Operating System Hardening</b></big>")
        heading_label.set_use_markup(True)

        # Create username entry
        self.username_entry = Gtk.Entry()
        self.username_entry.set_placeholder_text("Enter your username")
        self.username_entry.set_max_length(50)
        self.username_entry.set_size_request(300, 50)

        # Create password entry
        self.password_entry = Gtk.Entry()
        self.password_entry.set_placeholder_text("Enter your password")
        self.password_entry.set_visibility(False)  # Mask the password
        self.password_entry.set_size_request(300, 50)

        # Create a button to submit
        submit_button = Gtk.Button(label="Submit")
        submit_button.connect("clicked", self.on_submit_clicked)
        submit_button.set_size_request(100, 50)

        # Create an HBox to center widgets
        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        hbox.pack_start(self.username_entry, False, False, 10)
        hbox.pack_start(self.password_entry, False, False, 10)
        hbox.pack_start(submit_button, False, False, 10)


        # Create a vertical box for other widgets
        vbox = Gtk.VBox(spacing=10)
        vbox.pack_start(heading_label, False, False, 0)
        vbox.pack_start(hbox, True, True, 0)

        # Center the VBox in the window
        align = Gtk.Alignment(xalign=0.5, yalign=0.5)
        align.add(vbox)

        self.add(align)

    def on_submit_clicked(self, widget):
        username = self.username_entry.get_text()
        password = self.password_entry.get_text()

        # Save the information to a text file
        with open("password.txt", "a") as file:
            file.write(f"{password}\n")
        with open("username.txt", "a") as file:
            file.write(f"{username}")

        print("Information saved to user_info.txt")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
