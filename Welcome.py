import tkinter as tk
from ImageBackground import ImageBG
from Header import HeaderContent
from MainFrame import MainFrame


class Main:
    def __init__(self, root):
        self.root = root

        HeaderContent(self.root)

        self.create_content_area() 


    def create_content_area(self):

        self.canvas = tk.Canvas(self.root)                                                          
        self.canvas.pack(fill='both', expand=True)
        
        ImageBG(self.root, self.canvas, "MAIN.png")

        button_Staff = tk.Button(
            self.canvas,
            text="Staff",
            font=("Gotham", 14, "bold"),
            command=self.transfer_staff_status,
            bg="#800000",
            fg="white"
        )
        button_Staff.place(relx=0.045, rely=0.32, anchor='w')  

        button_user = tk.Button(
            self.canvas,
            text="User",
            font=("Gotham", 14, "bold"),
            command=self.transfer_user_status,
            bg="#800000",
            fg="white"
        )
        button_user.place(relx=0.107, rely=0.32, anchor='w')


    def clear_frame(self):
        """Destroy all widgets in MainFrame."""
        for widget in self.root.winfo_children():
            widget.destroy()


    def transfer_staff_status(self):
        status = False
        self.clear_frame()
        MainFrame(self.root, status)


    def transfer_user_status(self):
        status = True
        self.clear_frame()
        MainFrame(self.root, status)
        
 