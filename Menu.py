import tkinter as tk
from Toplevel import TopLevel
from ImageBackground import ImageBG


class Menu:
    def __init__(self, root):
        self.root = root


    def title_content_area(self, data):
        top_level = TopLevel(self.root)
        top_level.create_toplevel_frame("All Book's Title", data)


    def authors_content_area(self, data):
        top_level = TopLevel(self.root)
        top_level.create_toplevel_frame("All Writers", data)


    def genre_content_area(self, data):
        top_level = TopLevel(self.root)
        top_level.create_toplevel_frame("All Genre", data)


    def nationality_content_area(self, data):
        top_level = TopLevel(self.root)
        top_level.create_toplevel_frame("All Nationality", data)


    def history_content_area(self, data):
        top_level = TopLevel(self.root)
        top_level.create_toplevel_frame("All Era", data)


    def select_all_content(self, data):
        top_level = TopLevel(self.root)
        top_level.create_toplevel_frame("Select All Content", data)


    def about_us_content_area(self, root):
        top_level = tk.Toplevel(root)
        top_level.title('About Us')
        top_level.state('zoomed')

        self.canvas = tk.Canvas(top_level)
        self.canvas.pack(fill='both', expand=True)

        ImageBG(top_level, self.canvas, 'About_Us.png')

