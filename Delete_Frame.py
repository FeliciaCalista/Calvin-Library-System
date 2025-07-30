import tkinter as tk  
from ImageBackground import ImageBG 
from Header import HeaderContent 
from DatabaseExecution import DatabaseExecution


class Frame27(): 
    def __init__(self, root, text, label_text, value):
        self.root = root  
        self.text = text
        self.label_text = label_text
        self.value = value 
        self.search_entry = None

        self.key_map = {
            1: "book",
            2: "writer",
            3: "genre",
            4: "history",
            5: "nationality",
        }
        
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
            text=self.text, 
            font=("Gotham", 14, "bold"), 
            fg="#800000"  
        )
        content_title.grid(row=0, column=0, columnspan=4, pady=10)

        self.search_label = tk.Label(content_frame, text=self.label_text, fg='white', bg='#800000', width=15, height=1, font=("Gotham", 14, "bold"))
        self.search_label.grid(row=2, column=0, columnspan=4, pady=(20, 5), sticky="n")

        self.search_entry = tk.Entry(content_frame, font=("Gotham", 14))
        self.search_entry.grid(row=3, column=0, columnspan=4, pady=(5, 10), sticky="n")

        self.submit_button = tk.Button(
            content_frame,
            text="Delete",  
            font=("Gotham", 14, "bold"), 
            command=self.delete_data, 
            bg="#800000",  
            fg="white"  
        )
        self.submit_button.grid(row=4, column=0, columnspan=4, pady=(10, 0), sticky="n") 


    def delete_data(self):
        entry = self.search_entry.get()
        self.data = DatabaseExecution()

        delete_mapping = {
            1: self.data.delete_book,
            2: self.data.delete_writer,
            3: self.data.delete_genre,
            4: self.data.delete_history,
            5: self.data.delete_nationality
        }

        if self.value in delete_mapping:
            result = delete_mapping[self.value](entry)
            if result:
                self.root.quit()
            else:
                self.search_entry.delete(0, tk.END)
