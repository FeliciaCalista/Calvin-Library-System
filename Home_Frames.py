from Toplevel import TopLevel
from DatabaseExecution import DatabaseExecution

class Frame9:
    def __init__(self, root, keyword, value, username):
        self.root = root
        self.keyword = keyword
        self.value = value
        self.username = username

        self.d = DatabaseExecution()
        self.books = self.d.search_book(self.keyword)

        toplevel = TopLevel(self.root, True, self.value, username=self.username)
        toplevel.create_toplevel_frame('Home for Title', self.books)


class Frame10:
    def __init__(self, root, keyword, value, username):
        self.root = root
        self.keyword = keyword
        self.value = value
        self.username = username

        self.d = DatabaseExecution()
        self.writers = self.d.search_writer(self.keyword)

        toplevel = TopLevel(self.root, True, self.value, username=self.username)
        toplevel.create_toplevel_frame('Home for Writer', self.writers)


class Frame12:
    def __init__(self, root, keyword, value, username):
        self.root = root
        self.keyword = keyword
        self.value = value
        self.username = username

        self.d = DatabaseExecution()
        self.genre = self.d.search_book_genre(self.keyword)

        toplevel = TopLevel(self.root, True, self.value, username=self.username)
        toplevel.create_toplevel_frame('Home for Genre', self.genre)


class Frame11:
    def __init__(self, root, keyword, value, username):
        self.root = root
        self.keyword = keyword
        self.value = value
        self.username = username

        self.d = DatabaseExecution()
        self.year = self.d.search_book_published_year(self.keyword)

        toplevel = TopLevel(self.root, True, self.value, username=self.username)
        toplevel.create_toplevel_frame('Home for Published Year', self.year)

