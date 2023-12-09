import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango

class ContentsPage(Gtk.Window):
    def __init__(self):
        super().__init__(title="Contents Page")
        self.set_default_size(600, 400)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        text_view = Gtk.TextView()
        text_view.set_editable(False)
        text_view.set_cursor_visible(False)
        text_view.modify_font(Pango.FontDescription("12"))

        buffer = text_view.get_buffer()
        buffer.set_text("• Item 1\n• Item 2\n• Item 3\n• Item 4\n• Item 5")

        vbox.pack_start(text_view, True, True, 0)

if __name__ == "__main__":
    win = ContentsPage()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()