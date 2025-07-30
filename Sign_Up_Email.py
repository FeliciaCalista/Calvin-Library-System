import tkinter as tk  
from tkinter import messagebox
from ImageBackground import ImageBG 
from Header import HeaderContent
from Sign_Up_UP import Frame3
from Login import Frame4
from DatabaseExecution import DatabaseExecution


class Frame2(): 
    def __init__(self, root, status):
        self.root = root  
        self.email = None
        self.status = status 

        HeaderContent(self.root) 

        self.create_content_area()
         

    def create_content_area(self):
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill='both', expand=True)

        content_frame = tk.Frame(self.root, bg="#f5f5f5", padx=10, pady=10)  

        ImageBG(self.root, self.canvas, 'BACKGROUND.png')

        self.email_box_frame = tk.Frame(self.root, bg="white", padx=20, pady=20) 
        self.email_box_frame.place(relx=0.5, rely=0.5, anchor='center')  

        self.email_label = tk.Label(
            self.email_box_frame, 
            text='Email', 
            fg='white', 
            bg='#800000', 
            width=11, 
            height=1, 
            font=("Gotham", 14)
        )
        self.email_label.pack(pady=10)  # Menambahkan jarak antar elemen

        self.email_entry = tk.Entry(self.email_box_frame, font=("Gotham", 12), width=25)
        self.email_entry.pack(pady=10)

        self.submit_button = tk.Button(
            self.email_box_frame,
            text="Submit",  
            font=("Gotham", 14),  
            command=self.submit_email,  
            bg="#800000",  
            fg="white"  
        )
        self.submit_button.pack(pady=10)


    def submit_email(self):
        email = self.email_entry.get()

        self.data = DatabaseExecution()
        self.user_registered_emails = self.data.get_user_email()
        self.user_registered_emails = [i[0] for i in self.user_registered_emails]

        self.data = DatabaseExecution()
        self.staff_registered_emails = self.data.get_staff_email()
        self.staff_registered_emails = [i[0] for i in self.staff_registered_emails]

        if self.status:
            self.action(email, self.user_registered_emails)
        else:
            self.action(email, self.staff_registered_emails)


    def action(self, email, email_data):
        if email_data:
            if email in email_data:
                messagebox.showwarning("Email Already Registered", f"The email '{email}' is already registered.")
                self.root.after(10, self.show_frame4)
            else:
                messagebox.showinfo("Submitted Email", f"Email submitted: {email}")
                self.email = email
                self.root.after(10, self.show_frame3)
        else:
            messagebox.showinfo("Submitted Email", f"Email submitted: {email}")
            self.email = email
            self.root.after(10, self.show_frame3)


    def clear_frame(self):
        """Destroy all widgets in MainFrame."""
        for widget in self.root.winfo_children():
            widget.destroy() 


    def show_frame3(self):
        self.clear_frame()
        Frame3(self.root, self.email, self.status)


    def show_frame4(self):
        self.clear_frame()
        Frame4(self.root, self.status)

