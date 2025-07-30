import tkinter as tk  
from ImageBackground import ImageBG 
from Header import HeaderContent 
from DatabaseExecution import DatabaseExecution


class Frame26(): 
    def __init__(self, root):
        self.root = root 
        self.nationality_id_entry = None
        self.nationality_name_entry = None 
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
            text="Nationality", 
            font=("Gotham", 14, "bold"), 
            fg="#3b3b3b"  
        )
        content_title.grid(row=0, column=0, columnspan=4, pady=10)

        self.nationality_id_entry = self.create_label_entry(content_frame, "Nationality ID", 1)
        self.nationality_name_entry = self.create_label_entry(content_frame, "Nationality Name", 2)
        self.description_entry = self.create_label_entry(content_frame, "Description", 3)

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
        nationality_id = self.nationality_id_entry.get()
        nationality_name = self.nationality_name_entry.get()
        description = self.description_entry.get()

        self.data = DatabaseExecution()
        new_data = self.data.add_nationality(nationality_id, nationality_name, description)

        if new_data:
            self.root.quit()