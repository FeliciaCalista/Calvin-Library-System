import mysql.connector
from tkinter import messagebox
from DatabaseManager import DatabaseManager

class DatabaseExecution:
    def __init__(self):
        self.d = DatabaseManager('localhost', 'root', 'password', 'CalvinLibrary')
        self.d.connect()
        self.connection = self.d.get_db_connection()
        self.cursor = self.connection.cursor()
        self.s = DatabaseManager('localhost', 'root', 'password', 'CalvinLibrary')

        self.cursor.execute(f"USE {self.d.database_name}")


    def get_image_file_name(self):
        new_data = self.s.get_image_file()
        return new_data


    def add_book(self, Book_ID, Title, Writer_ID, Genre_ID, Publication_Year, Description, Availability_Status='Available', Cover_Image=None):
        try:
            book_query = """
            INSERT INTO Book (Book_ID, Title, Writer_ID, Genre_ID, Publication_Year, Availability_Status, Description, Cover_Image)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cover_image_blob = self.get_image_as_blob(Cover_Image) if Cover_Image else None
            new_data = (Book_ID, Title, Writer_ID, Genre_ID, Publication_Year, Availability_Status, Description, cover_image_blob)

            self.cursor.execute(book_query, new_data)

            self.d.commit_and_close()
            messagebox.showinfo('Success!', 'Book successfully added!')
        
        except mysql.connector.errors.IntegrityError as e:
            messagebox.showinfo('Error!', 'Please fill all the entry')
    

    def get_image_as_blob(self, image_filename):
        try:
            with open(image_filename, 'rb') as image_file:
                return image_file.read()
        except FileNotFoundError:
            print(f"File {image_filename} not found.")
            return None


    # DAFTAR BARU --> FRAME 2
    def add_user(self, username, password, email):
        self.cursor.execute('INSERT INTO User (Username, Password, Email, Book_ID) VALUES (%s, %s, %s, %s)', (username, password, email, None))
        self.d.commit_and_close()


    def add_genre(self, Genre_ID, Genre_Name, Description):
        try:
            self.cursor.execute('INSERT INTO Genre (Genre_ID, Genre_Name, Description) VALUES (%s, %s, %s)', (Genre_ID, Genre_Name, Description))
            self.d.commit_and_close()
            messagebox.showinfo('Success!', 'Book successfully added!')
        except mysql.connector.errors.IntegrityError as e:
            messagebox.showinfo('Error!', 'Please fill all the entry')


    def add_nationality(self, ID, Nationality_Name, Description):
        try:
            self.cursor.execute('INSERT INTO Nationality (ID, Nationality_Name, Description) VALUES (%s, %s, %s)', (ID, Nationality_Name, Description))
            self.d.commit_and_close()
            messagebox.showinfo('Success!', 'Book successfully added!')
        except mysql.connector.errors.IntegrityError as e:
            messagebox.showinfo('Error!', 'Please fill all the entry')


    def add_writer(self, Writer_ID, Name, Birth_Year, Nationality_ID, Biography):
        try:
            self.cursor.execute('INSERT INTO Writer (Writer_ID, Name, Birth_Year, Nationality_ID, Biography) VALUES (%s, %s, %s, %s, %s)', 
                                (Writer_ID, Name, Birth_Year, Nationality_ID, Biography))
            self.d.commit_and_close()
            messagebox.showinfo('Success!', 'Book successfully added!')
        except mysql.connector.errors.IntegrityError as e:
            messagebox.showinfo('Error!', 'Please fill all the entry')


    def add_history(self, id, era, description):
        try:
            self.cursor.execute('INSERT INTO History_of_Library (ID, Era, Description) VALUES (%s, %s, %s)', (id, era, description))
            self.d.commit_and_close()
            messagebox.showinfo('Success!', 'Book successfully added!')
        except mysql.connector.errors.IntegrityError as e:
            messagebox.showinfo('Error!', 'Please fill all the entry')


    # PEMINJAMAN BUKU --> FRAME 13 - 16
    def update_book_status(self, title):
        commands = f"""
                    UPDATE Book
                    SET Availability_Status = 'Not Available'
                    WHERE Title = %s"""
        self.cursor.execute(commands, (title,))
        self.d.commit_and_close()


    # PENGEMBALIAN BUKU
    def restore_book_status(self, book_id):
        commands = f"""
                    UPDATE Book
                    SET Availability_Status = 'Available'
                    WHERE Book_ID = %s"""
        self.cursor.execute(commands, (book_id,))
        self.d.commit_and_close()


    # FRAME 9
    def search_book(self, keyword):
        self.cursor.execute("""
                            SELECT Book.Title, Writer.Name, Book.Publication_Year, Genre.Genre_Name
                            FROM Book 
                            JOIN Writer ON Book.Writer_ID = Writer.Writer_ID 
                            JOIN Genre ON Book.Genre_ID = Genre.Genre_ID
                            WHERE Book.Title LIKE %s""",
                            (f"%{keyword}%",))
        result = self.cursor.fetchall()
        result.insert(0, ('Title', 'Writer', 'Published_Year', 'Genre'))
        self.d.commit_and_close()
        return result


    # FRAME 10
    def search_writer(self, keyword):
        self.cursor.execute("""
                    SELECT Book.Title, Writer.Name, Book.Publication_Year, Genre.Genre_Name
                    FROM Book JOIN Writer ON Book.Writer_ID = Writer.Writer_ID 
                    JOIN Genre ON Book.Genre_ID = Genre.Genre_ID
                    WHERE Writer.Name LIKE %s""",  (f"%{keyword}%",))
        result = self.cursor.fetchall()
        result.insert(0, ('Title', 'Writer', 'Published_Year', 'Genre'))
        self.d.commit_and_close()
        return result


    # FRAME 11
    def search_book_published_year(self, keyword):
        self.cursor.execute("""
                    SELECT Book.Title, Book.Publication_Year, Writer.Name, Genre.Genre_Name
                    FROM Book JOIN Writer ON Book.Writer_ID = Writer.Writer_ID 
                    JOIN Genre ON Book.Genre_ID = Genre.Genre_ID
                    WHERE Book.Publication_Year LIKE %s""",  (f"%{keyword}%",))
        result = self.cursor.fetchall()
        result.insert(0, ('Title', 'Published_Year', 'Writer', 'Genre'))
        self.d.commit_and_close()
        return result
    

    # FRAME 12
    def search_book_genre(self, keyword):
        self.cursor.execute("""
                    SELECT Book.Title, Genre.Genre_Name, Writer.Name, Book.Publication_Year
                    FROM Book JOIN Writer ON Book.Writer_ID = Writer.Writer_ID 
                    JOIN Genre ON Book.Genre_ID = Genre.Genre_ID
                    WHERE Genre.Genre_Name Like %s""",  (f"%{keyword}%",))
        result = self.cursor.fetchall()
        result.insert(0, ('Title', 'Genre', 'Writer', 'Published_Year'))
        self.d.commit_and_close()
        return result


    def get_all_book(self):
        self.cursor.execute('SELECT * FROM Book')
        result = self.cursor.fetchall()
        result.insert(0, ('Book_ID', 'Title', 'Writer_ID', 'Genre_ID', 'Publication_Year', 'Availability_Status', 'Description', 'Cover_Image'))
        self.d.commit_and_close()
        return result


    # SELECT ONLY BOOK WITHOUT WRITER AND GENRE --> FRAME 5 
    def get_book_data(self):
        self.cursor.execute('SELECT Book_ID, Title, Publication_Year, Availability_Status FROM Book')
        result = self.cursor.fetchall()
        result.insert(0, ('ID', 'Title', 'Publication_Year', 'Availability_Status'))
        self.d.commit_and_close()
        return result
    

    # MANY TO MANY RELATION (SELECT *) --> FRAME 7
    def get_all_book_data(self):
        self.cursor.execute('SELECT Book_ID, Title, Writer_ID, Genre_ID, Publication_Year, Availability_Status FROM Book')
        result = self.cursor.fetchall()
        result.insert(0, ('Book_ID','Title','Writer_ID','Genre_ID','Publication_Year','Availability_Status'))
        self.d.commit_and_close()
        return result


    # SHOW ONLY ONE BOOK --> FRAME 13
    def show_specific_book(self, title):
        self.cursor.execute('SELECT * FROM Book WHERE Title = %s', (title,))
        result = self.cursor.fetchall()
        result.insert(0, ('Book_ID','Title','Writer_ID','Genre_ID','Publication_Year','Availability_Status', 'Description', 'Cover_Image'))
        self.d.commit_and_close()
        return result

    
    def get_all_writers(self):
        self.cursor.execute('SELECT * FROM Writer')
        result = self.cursor.fetchall()
        result.insert(0, ('Writer_ID', 'Name', 'Birth_Year', 'Nationality_ID', 'Biography'))
        self.d.commit_and_close()
        return result

    # SELECT ONLY NAME --> FRAME 6
    def get_writers_name(self):
        self.cursor.execute('SELECT Name FROM Writer')
        result = self.cursor.fetchall()
        result.insert(0, ('Name'))
        self.d.commit_and_close()
        return result


    # SELECT * EXCEPT BIO --> FRAME 19
    def get_all_writer_data(self):
        self.cursor.execute('SELECT Writer_ID, Name, Birth_Year, Nationality_ID FROM Writer')
        result = self.cursor.fetchall()
        result.insert(0, ('Writer_ID','Name','Birth_Year','Nationality_ID'))
        self.d.commit_and_close()
        return result


    # SHOW ONLY ONE WRITER --> FRAME 20
    def show_specific_writer(self, writer):
        commands = f'SELECT * FROM Writer WHERE Name = %s'
        self.cursor.execute(commands, (writer,))
        result = self.cursor.fetchall()
        result.insert(0, ('Writer_ID','Name','Birth_Year','Nationality_ID','Biography'))
        self.d.commit_and_close()
        return result


    def get_all_history(self):
        self.cursor.execute('SELECT * FROM History_of_Library')
        result = self.cursor.fetchall()
        result.insert(0, ('ID', 'Era' 'Description'))
        self.d.commit_and_close()
        return result


    def get_history_data(self):
        commands = f'SELECT ID, Era FROM History_of_Library'
        self.cursor.execute(commands)
        result = self.cursor.fetchall()
        result.insert(0, ('ID', 'Era'))
        self.d.commit_and_close()
        return result
    

    def get_all_nationality(self):
        self.cursor.execute('SELECT * FROM Nationality')
        result = self.cursor.fetchall()
        result.insert(0, ('ID', 'Nationality_Name', 'Description'))
        self.d.commit_and_close()
        return result
    

    def get_nationality_data(self):
        commands = f'SELECT ID, Nationality_Name FROM Nationality'
        self.cursor.execute(commands)
        result = self.cursor.fetchall()
        result.insert(0, ('ID', 'Nationality'))
        self.d.commit_and_close()
        return result
    

    def get_all_genre(self):
        self.cursor.execute('SELECT * FROM Genre')
        result = self.cursor.fetchall()
        result.insert(0, ('Genre_ID', 'Genre_Name', 'Description'))
        self.d.commit_and_close()
        return result
    

    def get_genre_data(self):
        commands = f'SELECT Genre_ID, Genre_Name FROM Genre'
        self.cursor.execute(commands)
        result = self.cursor.fetchall()
        result.insert(0, ('ID', 'Genre'))
        self.d.commit_and_close()
        return result


    def get_all_user(self):
        self.cursor.execute('SELECT * FROM User')
        result = self.cursor.fetchall()
        result.insert(0, ('Username', 'Password', 'Email', 'Date'))
        self.d.commit_and_close()
        return result
    

    def get_user_email(self):
        commands = f'SELECT Email FROM User'
        self.cursor.execute(commands)
        result = self.cursor.fetchall()
        self.d.commit_and_close()
        return result


    def get_user_name_pass(self):
        commands = f'SELECT Username, Password FROM User'
        self.cursor.execute(commands)
        result = self.cursor.fetchall()
        self.d.commit_and_close()
        return result
    

    def insert_user_book(self, username, book_id):
        commands = f'''UPDATE User
                        SET Book_ID = %s
                        WHERE Username = %s'''
        self.cursor.execute(commands, (book_id, username))
        self.d.commit_and_close()


    def delete_user_book(self, username, book_ID):
        self.cursor.execute('SELECT Book_ID from User WHERE Username = %s', (username,))
        result = self.cursor.fetchall()
        result = result[0][0]
        if result == None:
            messagebox.showinfo('Error', "You didn't borrow any book!")
            return False
        elif result != book_ID:
            messagebox.showinfo('Error', 'This was not the book you borrow')
            return False
        else:
            commands = f'''UPDATE User
                            SET Book_ID = %s
                            WHERE Username = %s'''
            self.cursor.execute(commands, (None,username))
            self.d.commit_and_close()
            return True


    def insert_new_user(self, username, password, new_email):
        self.cursor.execute('INSERT INTO User (Username, Password, Book_ID, Email) VALUES (%s, %s, %s, %s)', (username, password, None, new_email))
        self.d.commit_and_close()


    def delete_book(self, book_id):
        self.cursor.execute('DELETE FROM Book WHERE Book_ID = %s', (book_id,))
        if self.cursor.rowcount == 0:
            messagebox.showinfo("Error", "No book found with the given book ID.")
            self.d.commit_and_close()
            return False, 0
        else:
            self.d.commit_and_close()
            return True
        

    def delete_writer(self, writer_name):
        self.cursor.execute('DELETE FROM Writer WHERE Name = %s', (writer_name,))
        if self.cursor.rowcount == 0:
            messagebox.showinfo("Error", "No writer found with the given name.")
            self.d.commit_and_close()
            return False, 0
        else:
            self.d.commit_and_close()


    def delete_genre(self, genre_name):
        self.cursor.execute('DELETE FROM Genre WHERE Genre_Name = %s', (genre_name,))
        if self.cursor.rowcount == 0:
            messagebox.showinfo("Error", "No genre found with the given genre.")
            self.d.commit_and_close()
            return False, 0
        else:
            self.d.commit_and_close()
            return True


    def delete_history(self, history_name):
        self.cursor.execute('DELETE FROM History_of_Library WHERE Era = %s', (history_name,))
        if self.cursor.rowcount == 0:
            messagebox.showinfo("Error", "No Era found with the given era.")
            self.d.commit_and_close()
            return False, 0
        else:
            self.d.commit_and_close()
            return True


    def delete_nationality(self, nationality):
        self.cursor.execute('DELETE FROM Nationality WHERE Nationality_Name = %s', (nationality,))
        if self.cursor.rowcount == 0:
            messagebox.showinfo("Error", "No Nationality found with the given nationality.")
            self.d.commit_and_close()
            return False, 0
        else:
            self.d.commit_and_close()
            return True


    def get_all_staff(self):
        self.cursor.execute('SELECT * FROM Staff')
        result = self.cursor.fetchall()
        result.insert(0, ('ID', 'Name', 'Email', 'Password', 'Date'))
        self.d.commit_and_close()
        return result
    

    def get_staff_email(self):
        commands = f'SELECT Email FROM Staff'
        self.cursor.execute(commands)
        result = self.cursor.fetchall()
        self.d.commit_and_close()
        return result


    def get_staff_name_pass(self):
        commands = f'SELECT Name, Password FROM Staff'
        self.cursor.execute(commands)
        result = self.cursor.fetchall()
        self.d.commit_and_close()
        return result

    
    def insert_new_staff(self, name, password, new_email):
        self.cursor.execute('INSERT INTO Staff (Name, Password, Email) VALUES (%s, %s, %s)', (name, password, new_email))
        self.d.commit_and_close()


    
    def delete_relation(self, username, book_id, data):
        if data:
            new_data = [j for _, j, _ in data]
        else:
            messagebox.showinfo('Error', 'No book is borrowed')
            return False
        if book_id not in new_data:
            messagebox.showinfo('Error', 'The book is not borrowed')
            return False
        else: 
            for _, id, user in data:
                if book_id == id and username == user:
                    self.cursor.execute('DELETE FROM Book_User WHERE Book_ID = %s', (book_id,))
                    self.d.commit_and_close()
                    return True
                else:
                    messagebox.showinfo('Error', "You didn't borrow this book!")
                    return False