import tkinter as tk 
from ImageBackground import ImageBG 
from Header import HeaderContent
from DatabaseExecution import DatabaseExecution


class Frame23(): 
    def __init__(self, root):
        self.root = root
        self.writer_id_entry = None
        self.name_entry = None
        self.birth_year_entry = None 
        self.nationality_entry = None
        self.biography_entry = None  
        
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
            text="Writer", 
            font=("Gotham", 14, "bold"), 
            fg="#3b3b3b"  
        )
        content_title.grid(row=0, column=0, columnspan=4, pady=10)

        self.writer_id_entry    = self.create_label_entry(content_frame, "Writer ID", 1)
        self.name_entry         = self.create_label_entry(content_frame, "Name", 2)
        self.birth_year_entry   = self.create_label_entry(content_frame, "Birth Year", 3)
        self.nationality_entry  = self.create_label_entry(content_frame, "Nationality ID", 4)
        self.biography_entry    = self.create_label_entry(content_frame, "Biography", 5)

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
        writer_id= self.writer_id_entry.get()
        name = self.name_entry.get()
        birth_year = self.birth_year_entry.get()
        nationality = self.nationality_entry.get()
        biography = self.biography_entry.get()

        self.data = DatabaseExecution()
        new_data = self.data.add_writer(writer_id, name, birth_year, nationality, biography)

        if new_data:
            self.root.quit()