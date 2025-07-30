import tkinter as tk
from Menu import Menu
from DatabaseExecution import DatabaseExecution


class HeaderContent:
    def __init__(self, root):
        self.root = root

        self.paned = tk.PanedWindow(self.root, orient='horizontal')  
        self.paned.pack(fill='x', padx=10, pady=10)  

        self.title_frame = tk.Frame(self.paned, bg="#800000")  
        self.title_frame.pack(fill='x', expand=True)  

        self.title_label = tk.Label(
            self.title_frame, 
            text="CALVIN LIBRARY SYSTEM",  
            font=("GOTHAM", 16, "bold"),  
            fg="white",  
            bg="#800000"  
        )
        self.title_label.pack(side='left', anchor='w', padx=10, pady=10)

        self.button_frame = tk.Frame(self.title_frame, bg="#800000")                                                          # Create a button frame for the menu buttons
        self.button_frame.pack(side='right', padx=10)

        self.create_description_menubutton(self.button_frame)
        self.create_menu_menubutton(self.button_frame)

    def create_description_menubutton(self, button_frame):                                                           # Create the Menubutton for Description
        description_menubutton = tk.Menubutton(
            button_frame,
            text="Description",
            font=("Gotham", 11, "bold"),
            bg="#FFFFFF",
            fg="maroon",
            relief='raised'                                                                                          # Gives it a raised appearance
        )
        
        description_menubutton.menu = tk.Menu(description_menubutton, tearoff=0)                                     # Create a menu
        description_menubutton['menu'] = description_menubutton.menu

        description_menubutton.menu.add_command(label="About Us", command=self.show_about_us)                        # Replace with your function
        description_menubutton.menu.add_command(label="History of Library", command=self.show_history)      # Replace with your function
        description_menubutton.pack(side='left', padx=5)                                                             # Pack the Menubutton


    def create_menu_menubutton(self, button_frame):                                                                  # Create the Menubutton for Menu
        menu_menubutton = tk.Menubutton(
            button_frame,
            text="Menu",
            font=("Gotham", 11, "bold"),
            bg="#FFFFFF",
            fg="maroon",
            relief='raised'  
        )

        menu_menubutton.menu = tk.Menu(menu_menubutton, tearoff=0)  
        menu_menubutton['menu'] = menu_menubutton.menu

        menu_menubutton.menu.add_command(label="All Books", command=self.show_books)  
        menu_menubutton.menu.add_command(label="All Writers", command=self.show_authors)  
        menu_menubutton.menu.add_command(label="All Genre", command=self.show_genre)
        menu_menubutton.menu.add_command(label="All Nationality", command=self.show_nationality)
        menu_menubutton.menu.add_command(label="Select All", command=self.show_all) 
        menu_menubutton.pack(side='left', padx=5) 


    def show_about_us(self):
        self.d = DatabaseExecution()
        menu = Menu(self.root)
        menu.about_us_content_area(self.root)


    def show_history(self):
        self.d = DatabaseExecution()
        menu = Menu(self.root)
        data = self.d.get_history_data()
        menu.history_content_area(data)
        

    def show_books(self):
        self.d = DatabaseExecution()
        menu = Menu(self.root)
        data = self.d.get_book_data()
        menu.title_content_area(data)


    def show_authors(self):
        self.d = DatabaseExecution()
        menu = Menu(self.root)
        data = self.d.get_all_writer_data()
        menu.authors_content_area(data)


    def show_genre(self):
        self.d = DatabaseExecution()
        menu = Menu(self.root)
        data = self.d.get_genre_data()
        menu.genre_content_area(data)


    def show_nationality(self):
        self.d = DatabaseExecution()
        menu = Menu(self.root)
        data = self.d.get_nationality_data()
        menu.nationality_content_area(data)


    def show_all(self):
        self.d = DatabaseExecution()
        menu = Menu(self.root)
        data = self.d.get_all_book_data()
        menu.select_all_content(data)