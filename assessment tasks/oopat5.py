class LibraryBook:
    library_name = "Python Library"
    total_books = 0
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        self.reader = "Нет"
        LibraryBook.total_books += 1
    
    def borrow(self, reader):
        if self.is_available:
            self.is_available = False
            self.reader = reader
            print(f"{self.title}: книга выдана читателю {reader}")
        else:
            print(f"{self.title}: книга уже выдана")
    
    def return_book(self):
        if not self.is_available:
            print(f"{self.title}: книга возвращена читателем {self.reader}")
            self.is_available = True
            self.reader = "Нет"
        else:
            print(f"{self.title}: книга уже находится в библиотеке")
    
    def show_info(self):
        if self.is_available:
            print(f'Книга "{self.title}" | Автор: {self.author} | Библиотека: {self.library_name} | Статус: доступна')
        else:
            print(f'Книга "{self.title}" | Автор: {self.author} | Библиотека: {self.library_name} | Статус: выдана читателю {self.reader}')
    
    def set_personal_library(self, library_name):
        self.library_name = library_name


title1 = input()
author1 = input()
title2 = input()
author2 = input()
reader1 = input()
reader2 = input()
new_library = input()
personal_library1 = input()

book1 = LibraryBook(title1, author1)
book2 = LibraryBook(title2, author2)

book1.borrow(reader1)
book2.borrow(reader2)

book2.borrow(reader1)

LibraryBook.library_name = new_library

book1.set_personal_library(personal_library1)

book1.return_book()

book1.show_info()
book2.show_info()

print(f"Всего книг: {LibraryBook.total_books}")