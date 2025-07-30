import tkinter as tk  
from ImageBackground import ImageBG
from DatabaseExecution import DatabaseExecution 
from Header import HeaderContent


class Frame22(): 
    def __init__(self, root):
        self.root = root  
        self.book_id_entry = None 
        self.title_entry = None
        self.writer_id_entry = None
        self.genre_id_entry = None
        self.publication_year_entry = None
        self.description_entry = None
        
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
            text="Title", 
            font=("Gotham", 14, "bold"), 
            fg="#800000"  
        )
        content_title.grid(row=0, column=0, columnspan=4, pady=10)

        self.book_id_entry          = self.create_label_entry(content_frame, "Book ID", 1,)
        self.title_entry            = self.create_label_entry(content_frame, "Title", 2)
        self.writer_id_entry        = self.create_label_entry(content_frame, "Writer ID", 3)
        self.genre_id_entry         = self.create_label_entry(content_frame, "Genre ID", 4)
        self.publication_year_entry = self.create_label_entry(content_frame, "Publication Year", 5)
        self.description_entry      = self.create_label_entry(content_frame, "Description", 6)
        self.cover_image_file_entry = self.create_label_entry(content_frame, "Cover Image File", 7)

        self.submit_button = tk.Button(
            content_frame,
            text="Add",  
            font=("Gotham", 14, "bold"),
            command=self.submit_data,  
            bg="#800000",  
            fg="white"  
        )
        self.submit_button.grid(row=14, column=0, columnspan=4, pady=(10, 0), sticky="n")  


    def create_label_entry(self, parent, label_text, row, entry_width=30):
        label = tk.Label(
            parent,
            text=label_text,
            font=("Gotham", 14, "bold"),
            fg="white",
            bg="#800000",
            width=15,
            anchor="w",
            padx=5
        )
        label.grid(row=row, column=0, padx=(5, 10), pady=5, sticky="e")

        entry = tk.Entry(parent, font=("Gotham", 12), width=entry_width)
        entry.grid(row=row, column=1, padx=(0, 10), pady=5, sticky="w")

        return entry


    def submit_data(self):
        book_id = self.book_id_entry.get()
        title = self.title_entry.get()
        writer_id = self.writer_id_entry.get()
        genre_id = self.genre_id_entry.get()
        publication_year = self.publication_year_entry.get()
        description = self.description_entry.get()
        cover_image_file = self.cover_image_file_entry.get() 

        self.data = DatabaseExecution()
        self.data.add_book(book_id, title, writer_id, genre_id, publication_year, description, Cover_Image=cover_image_file)
        self.root.quit()