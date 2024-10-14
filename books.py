import json

class Books:
    def __init__(self):
        self.file_path = 'books.json'
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.books, file)

    def display_books(self):
        if not self.books:
            print("Không có sách trong hệ thống.")
        else:
            for book in self.books:
                print(book)

    def add_book(self):
        new_book = {
            'title': input("Nhập tiêu đề sách: "),
            'author': input("Nhập tên tác giả: "),
            'year': input("Nhập năm xuất bản: ")
        }
        self.books.append(new_book)
        self.save_books()
        print("Sách đã được thêm thành công.")

    def update_book(self):
        title = input("Nhập tiêu đề sách cần cập nhật: ")
        for book in self.books:
            if book['title'] == title:
                book['author'] = input("Nhập tác giả mới: ")
                book['year'] = input("Nhập năm xuất bản mới: ")
                self.save_books()
                print("Sách đã được cập nhật.")
                return
        print("Không tìm thấy sách.")

    def delete_book(self):
        title = input("Nhập tiêu đề sách cần xóa: ")
        self.books = [book for book in self.books if book['title'] != title]
        self.save_books()
        print("Sách đã được xóa.")

    def search_books(self, keyword):
        results = [book for book in self.books if keyword.lower() in book['title'].lower()]
        if not results:
            print("Không tìm thấy sách.")
        else:
            for book in results:
                print(book)
