import tkinter as tk
from ImageBackground import ImageBG  
from Header import HeaderContent
from DatabaseExecution import DatabaseExecution


class Frame32:
    def __init__(self, root, username):
        self.root = root
        self.search_entry = None
        self.username = username

        HeaderContent(self.root)

        self.create_content_area()
    
    def create_content_area(self):
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill='both', expand=True)

        content_frame = tk.Frame(self.canvas, padx=10, pady=10)  
        content_frame.place(relx=0.5, rely=0.5, anchor="center")

        ImageBG(self.root, self.canvas)

        content_title = tk.Label(
            content_frame, 
            text="ENTER THE BOOK ID", 
            font=("Gotham", 14, "bold"), 
            fg="#800000"  
        )
        content_title.grid(row=0, column=0, columnspan=4, pady=10)

        self.search_entry = tk.Entry(content_frame, font=("Gotham", 14))
        self.search_entry.grid(row=3, column=0, columnspan=4, pady=(5, 10), sticky="n")

        self.submit_button = tk.Button(
            content_frame,
            text="Return",  
            font=("Gotham", 14, "bold"), 
            command=self.return_book, 
            bg="#800000",  
            fg="white"  
        )
        self.submit_button.grid(row=4, column=0, columnspan=4, pady=(10, 0), sticky="n") 


    def return_book(self):
        book_id = self.search_entry.get()
        self.d = DatabaseExecution()
        result = self.d.delete_user_book(self.username, book_id)
        if result:
            self.db = DatabaseExecution()
            self.db.restore_book_status(book_id)
            self.root.quit()