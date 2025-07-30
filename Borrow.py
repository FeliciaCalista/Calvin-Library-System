import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO
from DatabaseExecution import DatabaseExecution  


class Frame13:
    def __init__(self, root, search_title, search_entry, username):
        self.root = root
        self.search_title = search_title
        self.search_entry = search_entry
        self.username = username
        self.details_frame = None
        self.pinjam_button = None
        self.cancel_button = None
        
        self.db = DatabaseExecution()
        book_details = self.db.show_specific_book(self.search_title)  
        self.show_book_details(book_details[1])  


    def create_button(self, text, command, bg, fg, relx, rely):
        """Membuat tombol dengan parameter yang dapat disesuaikan."""
        button = tk.Button(
            self.root,
            text=text,
            command=command,
            fg=fg,
            bg=bg,
            width=11,
            height=1,
            font=("Gotham", 14)
        )
        button.place(relx=relx, rely=rely, anchor='center')
        return button       

    def show_book_details(self, book):
        """Menampilkan detail buku dalam frame baru."""
        if self.details_frame is not None:
            self.details_frame.destroy()

        self.details_frame = tk.Frame(self.root, bg="white", bd=2, relief=tk.RAISED)
        self.details_frame.place(relx=0.5, rely=0.53, anchor='center', width=400, height=450)

        # Menampilkan detail buku
        tk.Label(self.details_frame, text=f"Book Title: {book[1]}", bg="white", font=("Gotham", 14)).pack(pady=10)
        tk.Label(self.details_frame, text=f"Status: {book[5]}", bg="white", font=("Gotham", 14)).pack(pady=10)

        # Menampilkan gambar cover jika tersedia
        cover_image = book[7]
        if cover_image:
            self.display_book_cover(cover_image)
        else:
            tk.Label(self.details_frame, text="Image not found", bg="white", font=("Gotham", 12)).pack(pady=10)

        # Tombol Pinjam dan Cancel
        self.pinjam_button = self.create_button(
            text="Borrow",
            command=lambda: self.pinjam_buku(book[1], book[0]),
            bg="#800000",
            fg="white",
            relx=0.5,
            rely=0.74  # Atur posisi tombol Pinjam
        )
        self.pinjam_button.config(state=tk.NORMAL if book[5].lower() == "available" else tk.DISABLED)

        self.cancel_button = self.create_button(
            text="Cancel",
            command=self.cancel_book_details,
            bg="#800000",
            fg="white",
            relx=0.5,
            rely=0.68  # Atur posisi tombol Cancel
        )

    def cancel_book_details(self):
        """Menutup detail buku dan membersihkan Entry serta tombol."""
        self.details_frame.destroy()  # Hapus frame detail buku
        self.pinjam_button.destroy()  # Hapus tombol Pinjam
        self.cancel_button.destroy()  # Hapus tombol Cancel
        self.search_entry.delete(0, tk.END)  # Hapus teks di Entry


    def pinjam_buku(self, book, id):
        """Mengubah status buku menjadi 'not available'."""
        # Perbarui status buku di database
        self.db = DatabaseExecution()
        self.db.update_book_status(book)
        self.db = DatabaseExecution()
        self.db.insert_user_book(self.username, id)
        self.root.quit()


    def display_book_cover(self, image_blob):
        """Menampilkan gambar cover buku."""
        try:
            image_data = BytesIO(image_blob)
            image = Image.open(image_data)
            image = image.resize((150, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            image_label = tk.Label(self.details_frame, image=photo, bg="white")
            image_label.image = photo
            image_label.pack(pady=10)
        except Exception as e:
            print(f"Error loading image: {e}")
            messagebox.showerror("Error", "Gambar tidak dapat dimuat.")

