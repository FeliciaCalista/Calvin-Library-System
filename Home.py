import tkinter as tk  
from tkinter import ttk, messagebox
from ImageBackground import ImageBG 
from Header import HeaderContent 
from Home_Frames import Frame9
from Home_Frames import Frame10
from Home_Frames import Frame11
from Home_Frames import Frame12


class Frame8(): 
    def __init__(self, root, username):
        self.root = root 
        self.rbutton_result = None 
        self.username = username 
        
        HeaderContent(self.root)

        self.create_content_area()

    def create_content_area(self):
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill='both', expand=True)

        content_frame = tk.Frame(self.canvas, padx=20, pady=10)  
        content_frame.place(relx=0.5, rely=0.5, anchor="center")
   
        ImageBG(self.root, self.canvas)              

        content_title = tk.Label(
            content_frame, 
            text="PICK & SEARCH", 
            font=("Gotham", 14, "bold"), 
            fg="#800000"  
        )
        content_title.grid(row=0, column=0, columnspan=4, pady=10)

        self.rbutton_result = tk.IntVar()

        Rbutton_title = ttk.Radiobutton(content_frame, text="Book", variable=self.rbutton_result, value=1)
        Rbutton_title.grid(row=1, column=0, padx=5, pady=5)

        Rbutton_writer = ttk.Radiobutton(content_frame, text="Writer", variable=self.rbutton_result, value=2)
        Rbutton_writer.grid(row=1, column=1, padx=5, pady=5)

        Rbutton_year = ttk.Radiobutton(content_frame, text="Year", variable=self.rbutton_result, value=3)
        Rbutton_year.grid(row=1, column=2, padx=5, pady=5)

        Rbutton_genre = ttk.Radiobutton(content_frame, text="Genre", variable=self.rbutton_result, value=4)
        Rbutton_genre.grid(row=1, column=3, padx=5, pady=5)

        self.search_label = tk.Label(content_frame, text='Keyword', fg='#800000', width=11, height=1, font=("Gotham", 12, 'bold'))
        self.search_label.grid(row=2, column=0, columnspan=4, pady=(20, 5), sticky="n")

        self.search_entry = tk.Entry(content_frame, font=("Gotham", 14))
        self.search_entry.grid(row=3, column=0, columnspan=4, pady=(5, 10), sticky="n")

        self.submit_button = tk.Button(
            content_frame,
            text="Submit",  
            font=("Gotham", 14),  
            command=self.submit,  
            bg="#800000",  
            fg="white"  
        )
        self.submit_button.grid(row=4, column=0, columnspan=4, pady=(10, 0), sticky="n")

    def submit(self):
        keyword = self.search_entry.get()
        value = self.rbutton_result.get()
        if value == 1:
            Frame9(self.root, keyword, value, self.username)
        elif value == 2:
            Frame10(self.root, keyword, value, self.username)
        elif value == 3:
            Frame11(self.root, keyword, value, self.username)
        elif value == 4:
            Frame12(self.root, keyword, value, self.username)
