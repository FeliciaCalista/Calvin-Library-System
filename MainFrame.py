import tkinter as tk
from ImageBackground import ImageBG
from Header import HeaderContent
from Sign_Up_Email import Frame2
from Login import Frame4
from DatabaseExecution import DatabaseExecution


class MainFrame:
    def __init__(self, root, status):
        self.status = status
        self.root = root

        HeaderContent(self.root)

        self.db = DatabaseExecution()

        self.create_content_area() 


    def create_content_area(self):

        self.canvas = tk.Canvas(self.root)                                                          
        self.canvas.pack(fill='both', expand=True)
        
        ImageBG(self.root, self.canvas, 'BACKGROUND.png')

        if self.status:
            button_sign_up = tk.Button(
                self.canvas,
                text="Sign Up",
                font=("Gotham", 14, "bold"),
                command=self.sign_up,
                bg="#800000",
                fg="white"
            )
            button_sign_up.place(relx=0.03, rely=0.39, anchor='w')  

        button_login = tk.Button(
            self.canvas,
            text="Login",
            font=("Gotham", 14, "bold"),
            command=self.login,
            bg="#800000",
            fg="white"
        )
        if self.status:
            button_login.place(relx=0.11, rely=0.39, anchor='w')
        else:
            button_login.place(relx=0.03, rely=0.39, anchor='w')


    def clear_mainframe(self):
        """Destroy all widgets in MainFrame."""
        for widget in self.root.winfo_children():
            widget.destroy()  


    def sign_up(self):
        self.clear_mainframe()
        Frame2(self.root, self.status)
        

    def login(self):
        self.clear_mainframe()
        Frame4(self.root, self.status)
        
               