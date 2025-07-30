import mysql.connector
import csv


class DatabaseManager:
    def __init__(self, host, user, password, database_name):
        self.host = host
        self.user = user
        self.password = password
        self.database_name = database_name
        self.connection = None
        self.cursor = None
        self.image_file = []

        self.connect()

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        self.cursor = self.connection.cursor()

        if not self.database_exists():
            print(f"Database {self.database_name} does not exist, creating...")
            self.create_database() 
            self.create_tables()
            self.insert_data() 

        self.connection.database = self.database_name


    def database_exists(self):
        """Check if the database already exists."""
        self.cursor.execute("SHOW DATABASES LIKE %s", (self.database_name,))
        result = self.cursor.fetchone()
        return result is not None
    

    def drop_database(self):
        """Drops the existing database."""
        try:
            self.cursor.execute(f"DROP DATABASE IF EXISTS {self.database_name}")
            print(f"Database {self.database_name} dropped successfully.")
        except mysql.connector.Error as err:
            print(f"Error dropping database: {err}")


    def get_db_connection(self):
        return self.connection
    

    def create_database(self):
        self.cursor.execute(f"DROP DATABASE IF EXISTS {self.database_name}")
        self.cursor.execute(f"CREATE DATABASE {self.database_name}")
        self.cursor.execute(f"USE {self.database_name}")


    def create_tables(self):
        tables = [
            ("""
            CREATE TABLE IF NOT EXISTS Nationality (
                ID VARCHAR(10) PRIMARY KEY,
                Nationality_Name VARCHAR(100),
                Description TEXT
            ) engine = InnoDB
            """),

            ("""
            CREATE TABLE IF NOT EXISTS Writer (
                Writer_ID VARCHAR(50) UNIQUE PRIMARY KEY,
                Name VARCHAR(100),
                Birth_Year VARCHAR(10),
                Nationality_ID VARCHAR(100),
                Biography TEXT,
                FOREIGN KEY (Nationality_ID) REFERENCES Nationality(ID),
                FULLTEXT INDEX writer_search (Name)
            ) engine = InnoDB
            """),

            ("""
            CREATE TABLE IF NOT EXISTS Genre (
                Genre_ID VARCHAR(50) PRIMARY KEY,
                Genre_Name VARCHAR(100),
                Description TEXT,
                FULLTEXT INDEX genre_search (Genre_Name)
            ) engine = InnoDB
            """),

            ("""
            CREATE TABLE IF NOT EXISTS Book (
                Book_ID VARCHAR(50) PRIMARY KEY,
                Title VARCHAR(100),
                Writer_ID VARCHAR(50),
                Genre_ID VARCHAR(50),
                Publication_Year VARCHAR(10),
                Availability_Status ENUM('Available', 'Not Available'),
                Description TEXT,
                Cover_Image BLOB,
                FOREIGN KEY (Writer_ID) REFERENCES Writer(Writer_ID),
                FOREIGN KEY (Genre_ID) REFERENCES Genre(Genre_ID),
                FULLTEXT INDEX book_search (Title)
            ) engine = InnoDB
            """),

            ("""
            CREATE TABLE IF NOT EXISTS User (
                Username VARCHAR(100) PRIMARY KEY,
                Password VARCHAR(100),
                Email VARCHAR(100),
                Book_ID VARCHAR(100) NULL,
                Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (Book_ID) REFERENCES Book(Book_ID),
                FULLTEXT INDEX user_search (Username, Email)
            ) engine = InnoDB
            """),

            ("""
            CREATE TABLE IF NOT EXISTS Staff (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(100),
                Email Varchar(100),
                Password VARCHAR(10),
                Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FULLTEXT INDEX user_search (Name, Email)
            ) engine = InnoDB
            """),

            ("""
            CREATE TABLE IF NOT EXISTS History_of_Library (
                ID VARCHAR(50) PRIMARY KEY,
                Era VARCHAR(100),
                Description TEXT
            ) engine = InnoDB
            """)
            
        ]

        try:
            for table in tables:
                self.cursor.execute(table)
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error creating tables: {err}")
            self.connection.commit()


    def get_image_file(self):
        return self.image_file
    

    def insert_data(self):
        nationality = self.read_nationality_data()
        nationality_headers = nationality[0]
        nationality_data = nationality[1:]

        writers = self.read_writers_data()
        writers_headers = writers[0]
        writers_data = writers[1:]

        genre = self.read_genre_data()
        genre_headers = genre[0]
        genre_data = genre[1:]

        book = self.read_book_data()
        book_headers = book[0]
        book_data = book[1:]

        history = self.read_history_data()
        history_headers = history[0]
        history_data = history[1:]

        user = self.read_user_data()
        if user != []:
            user_headers = user[0]
            user_data = user[1:]
            user_query = f'INSERT IGNORE INTO User {user_headers} VALUES (%s, %s, %s, %s, %s)'.replace("'", "")
            for data in user_data:
                if len(data) < 5:
                    data = (data[0],data[1],data[2],None,data[3])
                    self.cursor.execute(user_query, data)
                else:
                    self.cursor.execute(user_query, data)

        staff = self.read_staff_data()
        if staff != []:
            staff_headers = staff[0]
            staff_data = staff[1:]
            staff_query = f'INSERT IGNORE INTO Staff {staff_headers} VALUES (%s, %s, %s, %s, %s)'.replace("'", "")
            self.cursor.executemany(staff_query, staff_data)

        nationality_query = f'INSERT IGNORE INTO Nationality {nationality_headers} VALUES (%s, %s, %s)'.replace("'", "")
        self.cursor.executemany(nationality_query, nationality_data)

        writer_query =  f'INSERT IGNORE INTO Writer {writers_headers} VALUES (%s, %s, %s, %s, %s)'.replace("'", "")
        self.cursor.executemany(writer_query, writers_data)

        genre_query = f'INSERT IGNORE INTO Genre {genre_headers} VALUES (%s, %s, %s)'.replace("'", "")
        self.cursor.executemany(genre_query, genre_data)

        # Memasukkan data buku dengan gambar
        book_query = f'INSERT IGNORE INTO Book {book_headers} VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'.replace("'", "")

        # Membaca gambar dan mengubahnya menjadi BLOB
        def get_image_as_blob(image_filename):
            try:
                with open(image_filename, 'rb') as image_file:
                    return image_file.read()
            except FileNotFoundError:
                print(f"File {image_filename} tidak ditemukan.")
                return None

        # Membaca data buku dan mengubah gambar menjadi BLOB
        for row in book_data:
            if len(row) != 8:
                print(f"Warning: Baris data tidak memiliki jumlah kolom yang sesuai. Ditemukan {len(row)} kolom: {row}")
                continue  

            book_id, title, writer_id, genre_id, publication_year, availability_status, description, cover_image = row
            self.image_file.append(cover_image)
            cover_image_blob = get_image_as_blob(cover_image)

            # Menyusun data untuk dimasukkan ke dalam query
            data = (book_id, title, writer_id, genre_id, publication_year, availability_status, description, cover_image_blob)
            self.cursor.execute(book_query, data)

        history_query = f'INSERT IGNORE INTO History_of_Library {history_headers} VALUES (%s, %s, %s)'.replace("'", "")
        self.cursor.executemany(history_query, history_data)

        self.connection.commit()


    def read_files(self, filename):
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            data = [tuple(row) for row in csv_reader]  
        return data
    

    def read_writers_data(self):
        return self.read_files('writer.csv')


    def read_genre_data(self):
        return self.read_files('genre.csv')


    def read_book_data(self):
        return self.read_files('book.csv')


    def read_history_data(self):
        return self.read_files('history.csv')


    def read_nationality_data(self):
        return self.read_files('nationality.csv')
    

    def read_user_data(self):
        return self.read_files('user.csv')
    

    def read_staff_data(self):
        return self.read_files('staff.csv')


    def commit_and_close(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close() 
