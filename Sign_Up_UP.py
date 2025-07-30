import tkinter as tk
from tkinter import messagebox
from ImageBackground import ImageBG
from Header import HeaderContent
from User_Action import Frame7_5
from Home_Staff import Frame21
from DatabaseExecution import DatabaseExecution


class Frame3(): 
    def __init__(self, root, new_email, status):
        self.root = root  
        self.username = None
        self.password = None 
        self.new_email = new_email
        self.status = status
        self.username_entry = None

        HeaderContent(self.root)

        self.data = DatabaseExecution()
        self.user = self.data.get_user_name_pass()
        self.user = [i for i, _ in self.user]

        self.data = DatabaseExecution()
        self.staff = self.data.get_staff_name_pass()

        self.create_content_area()
         
    def create_content_area(self):
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill='both', expand=True)

        content_frame = tk.Frame(self.root, bg="#f5f5f5", padx=10, pady=10)  
        ImageBG(self.root, self.canvas, 'BACKGROUND.png')

        form_frame = tk.Frame(self.root, bg="white", padx=20, pady=20)
        form_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.username_label = tk.Label(form_frame, text='Username', fg='white', bg='#800000', width=11, height=1, font=("Gotham", 14))
        self.username_label.pack(pady=(0, 5))

        self.username_entry = tk.Entry(form_frame, width=30)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(form_frame, text='Password', fg='white', bg='#800000', width=11, height=1, font=("Gotham", 14))
        self.password_label.pack(pady=(10, 5))

        self.password_entry = tk.Entry(form_frame, show='*', width=30)
        self.password_entry.pack(pady=5)

        self.submit_button = tk.Button(
            form_frame,
            text="Submit",  
            font=("Gotham", 14),  
            command=self.submit_username_password,  
            bg="#800000",  
            fg="white"  
        )
        self.submit_button.pack(pady=(15, 0))

    def submit_username_password(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.status:
            self.action(username, password, self.user)
        else:
            self.action(username, password, self.staff)


    def action(self, username, password, data):
        if username in self.user:
            messagebox.showwarning("Username Taken", f"The username '{username}' is already taken. Please choose another.")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            self.username = username
            self.password = password
            print(self.username, self.password, self.new_email)
            self.insert_new_data(username)

    
    def insert_new_data(self, username):
        self.data = DatabaseExecution()
        if self.status:
            self.data.insert_new_user(self.username, self.password, self.new_email)
            self.show_frame7_5(username)
        else:
            result = self.data.insert_new_staff(self.username, self.password, self.new_email)
            self.show_frame21()



    def get_username_pass(self):
        return self.username, self.password
    

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
