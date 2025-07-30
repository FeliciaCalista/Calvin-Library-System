import tkinter as tk  
from ImageBackground import ImageBG 
from Home import Frame8
from Header import HeaderContent 
from Return import Frame32


class Frame7_5:
    def __init__(self, root, username):
        self.root = root  
        self.username = username 
        
        HeaderContent(self.root)

        self.create_content_area()

    def create_content_area(self):
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill='both', expand=True)

        ImageBG(self.root, self.canvas)

        button_frame = tk.Frame(self.canvas, bg="white", padx=20, pady=20)  
        button_frame.place(relx=0.5, rely=0.5, anchor='center') 
        button_borrow = tk.Button(
            button_frame,
            text="Borrow",
            font=("Gotham", 14, "bold"),
            command=self.show_frame8,
            bg="#800000",
            fg="white",
            width=12
        )
        button_borrow.pack(pady=10)

        button_return = tk.Button(
            button_frame,
            text="Return",
            font=("Gotham", 14, "bold"),
            command=self.show_frame32,
            bg="#800000",
            fg="white",
            width=12
        )
        button_return.pack(pady=10)  


    def clear_frame(self):
        """Destroy all widgets in MainFrame."""
        for widget in self.root.winfo_children():
            widget.destroy() 


    def show_frame8(self):
        self.clear_frame()
        Frame8(self.root, self.username)


    def show_frame32(self):
        self.clear_frame()
        Frame32(self.root, self.username)

