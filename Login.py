import tkinter as tk
from tkinter import messagebox  
from ImageBackground import ImageBG 
from Header import HeaderContent
from User_Action import Frame7_5
from Home_Staff import Frame21
from DatabaseExecution import DatabaseExecution


class Frame4:
    def __init__(self, root, user_staff_status):
        self.root = root
        self.status = None
        self.user_staff_status = user_staff_status

        HeaderContent(self.root)

        self.data = DatabaseExecution()
        self.user_database = {username: password for username, password in self.data.get_user_name_pass()}

        self.data = DatabaseExecution()
        self.staff_database = {username: password for username, password in self.data.get_staff_name_pass()}

        self.create_content_area()

    def create_content_area(self):
        # Membuat canvas
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Menginisialisasi ImageBG
        self.image_bg = ImageBG(self.root, self.canvas, 'BACKGROUND.png')
        
        # Menambahkan entry untuk username
        self.username_label = tk.Label(self.root, text="Username", fg="white", bg="#800000", width=11, height=1, font=("Arial", 14))
        self.username_label.place(relx=0.5, rely=0.41, anchor='center')
        self.username_entry = tk.Entry(self.root)
        self.username_entry.place(relx=0.5, rely=0.45, anchor='center')

        # Menambahkan entry untuk password
        self.password_label = tk.Label(self.root, text="Password", fg="white", bg="#800000", width=11, height=1, font=("Arial", 14))
        self.password_label.place(relx=0.5, rely=0.5, anchor='center')
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.place(relx=0.5, rely=0.54, anchor='center')

        # Menambahkan tombol submit
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit, fg="white", bg="#800000", width=11, height=1, font=("Arial", 14))
        self.submit_button.place(relx=0.5, rely=0.6, anchor='center')

        
    def submit(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showinfo("Error", "Username and Password is missing")
            print(f"Username: {username}, Password: {password}")
        else:
            if self.user_staff_status:
                self.check(username, password, self.user_database)
            else:
                self.check(username, password, self.staff_database)


    def check(self, username, password, database):
        # Memeriksa apakah username dan password valid
        if username in database and database[username] == password:
            print(f"Username: {username}, Password: {password} - Succesfully Login!")
            self.status = 'Valid'

            if self.user_staff_status:
                self.show_frame7_5(username)
            else:
                self.show_frame21()
                
        else:
            messagebox.showinfo("Error", "Username or Password is invalid.")
            print(f"Username: {username}, Password: {password} - Login failed.")


    def get_status(self):
        return self.status
    

    def clear_frame(self):
        """Destroy all widgets in MainFrame."""
        for widget in self.root.winfo_children():
            widget.destroy() 


    def show_frame7_5(self, username):
        self.clear_frame()
        Frame7_5(self.root, username)


    def show_frame21(self):
        self.clear_frame()
        Frame21(self.root)
