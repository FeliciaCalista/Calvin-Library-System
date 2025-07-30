import tkinter as tk
from tkinter import ttk
from ImageBackground import ImageBG
from Borrow import Frame13
from tkinter import messagebox


class TopLevel:
    def __init__(self, root, status=False, value=None, username=None):
        self.status = status
        self.root = root
        self.value = value
        self.username = username
        self.search_result = None
        self.search_button = None
        self.data = None


    def create_toplevel_frame(self, title, data):
        new_window = tk.Toplevel(self.root)
        new_window.title(title)
        new_window.state('zoomed')
        self.data = [i[0] for i in data]

        self.canvas = tk.Canvas(new_window)
        self.canvas.pack(fill='both', expand=True)

        ImageBG(new_window, self.canvas, 'BACKGROUND.png')

        self.make_scrollbar(new_window, data)


    def make_scrollbar(self, toplevel, data):
        frame = tk.Frame(toplevel)
        frame.pack(fill='both', expand=True, padx=10, pady=10)

        self.scrollbar = tk.Scrollbar(frame, orient="vertical")

        self.tree = ttk.Treeview(frame, columns=data[0], show='headings', yscrollcommand=self.scrollbar.set)

        style = ttk.Style()
        style.configure("Treeview.Heading",
                        font=("Gotham", 11, "bold"),      
                        foreground="#800000",             
                        background="#4CAF50"             
                        )

        for i in data[0]:
            self.tree.heading(i, text=i)
            self.tree.column(i, anchor='center')

        self.tree.pack(side='left', fill='both', expand=True)

        self.scrollbar.config(command=self.tree.yview)
        self.scrollbar.pack(side='right', fill='y')

        self.populate_treeview(data[1:])

        self.canvas.create_window(self.root.winfo_screenwidth() // 2, self.root.winfo_screenheight() // 2, window=frame, anchor='center')
        self.tree.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        if self.status:
            self.search_entry(toplevel)


    def populate_treeview(self, data):
        for row in data:
            self.tree.insert('', 'end', values=row)


    def search_entry(self, toplevel):
        self.search_label = tk.Label(toplevel, text="Enter the Specific Book Title", fg="white", bg="#800000", font=("Gotham", 12, 'bold'))
        self.search_label.place(relx=0.5, rely=0.8, anchor='center')

        self.search_result = tk.Entry(toplevel, width=50)
        self.search_result.place(relx=0.5, rely=0.85, anchor='center')

        self.search_button = tk.Button(toplevel, text="Submit", fg="white", bg="#800000", command=self.check_typo, font=("Gotham", 14))
        self.search_button.place(relx=0.5, rely=0.9, anchor='center')

        self.message_label = tk.Label(toplevel, text="", bg='white', fg='red')
        self.message_label.place(relx=0.5, rely=0.97, anchor='center')


    def check_typo(self):
        keyword = self.search_result.get().strip()
        if keyword in self.data:
            messagebox.showinfo('Success', 'Book Found')
            self.transition_to_new_frame()
        else:
            messagebox.showinfo("Error", "Book Not Found. Please enter specific title.")
            self.search_result.delete(0, tk.END)  # Clear the entry field
            self.search_result.focus_set()  # Bring focus back to the entry field


    def transition_to_new_frame(self):
        search_result = self.search_result.get()
        Frame13(self.root, search_result, self.search_result, self.username)
        
