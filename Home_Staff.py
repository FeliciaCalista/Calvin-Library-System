import tkinter as tk  
from tkinter import ttk
from tkinter import messagebox
from ImageBackground import ImageBG 
from Header import HeaderContent 
from Add_Book import Frame22
from Add_Writer import Frame23
from Add_Genre import Frame24
from Add_History import Frame25
from Add_Nationality import Frame26
from Delete_Frame import Frame27


class Frame21(): 
    def __init__(self, root):
        self.root = root  
        self.rbutton_result = None 
        
        HeaderContent(self.root)

        self.create_content_area()

    def create_content_area(self):
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill='both', expand=True)

        content_frame = tk.Frame(self.canvas, padx=30, pady=30)  
        content_frame.place(relx=0.5, rely=0.5, anchor="center", width=600, height=200)
   
        ImageBG(self.root, self.canvas)   

        content_title = tk.Label(
            content_frame, 
            text="PICK & SELECT THE ACTION", 
            font=("Gotham", 16, "bold"), 
            fg="#800000"  
        )
        content_title.grid(row=0, column=0, columnspan=5, pady=8)
        self.rbutton_result = tk.IntVar()

        Rbutton_title = ttk.Radiobutton(content_frame, text="Book", variable=self.rbutton_result, value=1)
        Rbutton_title.grid(row=1, column=0, padx=8, pady=2, sticky="nsew")

        Rbutton_writer = ttk.Radiobutton(content_frame, text="Writer", variable=self.rbutton_result, value=2)
        Rbutton_writer.grid(row=1, column=1, padx=8, pady=2, sticky="nsew")

        Rbutton_year = ttk.Radiobutton(content_frame, text="Genre", variable=self.rbutton_result, value=3)
        Rbutton_year.grid(row=1, column=2, padx=8, pady=2, sticky="nsew")

        Rbutton_history = ttk.Radiobutton(content_frame, text="History", variable=self.rbutton_result, value=4)
        Rbutton_history.grid(row=1, column=3, padx=8, pady=2, sticky="nsew")

        Rbutton_nasionality = ttk.Radiobutton(content_frame, text="Nationality", variable=self.rbutton_result, value=5)
        Rbutton_nasionality.grid(row=1, column=4, padx=8, pady=2, sticky="nsew")

        # Buttons
        self.add_button = tk.Button(
            content_frame,
            text="Add",
            font=("Gotham", 12, "bold"),
            command=self.add,
            bg="#800000",
            fg="white",
        )
        self.add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=(12, 0), sticky="nsew")

        self.delete_button = tk.Button(
            content_frame,
            text="Delete",
            font=("Gotham", 12, "bold"),
            command=self.delete,
            bg="#800000",
            fg="white",
        )
        self.delete_button.grid(row=2, column=3, columnspan=2, padx=5, pady=(12, 0), sticky="nsew")

        # Configure grid weights for alignment
        for i in range(5):
            content_frame.grid_columnconfigure(i, weight=1, uniform="column")
        content_frame.grid_rowconfigure(0, weight=1)  # Title row
        content_frame.grid_rowconfigure(1, weight=1)  # Radiobuttons
        content_frame.grid_rowconfigure(2, weight=1)  # Buttons


    def clear_frame(self):
        """Destroy all widgets in MainFrame."""
        for widget in self.root.winfo_children():
            widget.destroy() 


    def add(self):
        value = self.rbutton_result.get()
        self.clear_frame()
        if value == 1:
            Frame22(self.root)
        elif value == 2:
            Frame23(self.root)
        elif value == 3:
            Frame24(self.root)
        elif value == 4:
            Frame25(self.root)
        elif value == 5:
            Frame26(self.root)
    

    def delete(self):
        value = self.rbutton_result.get()
        if value == 1:
            self.clear_frame()
            Frame27(self.root, 'Book_ID', 'Enter the Book ID', value)
        elif value == 2:
            messagebox.showinfo('Caution!', 'Deleting writer can cause missing book')
        elif value == 3:
            messagebox.showinfo('Caution!', 'Deleting genre can cause missing book')
        elif value == 4:
            self.clear_frame()
            Frame27(self.root, 'History', 'Enter the Era', value)
        elif value == 5:
            messagebox.showinfo('Caution!', 'Deleting nationality can cause missing book')

            