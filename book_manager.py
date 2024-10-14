import pandas as pd
import re

class BookManager:
    def __init__(self):
        try:
            # Tải dữ liệu từ file CSV
            self.books = pd.read_csv('books.csv')
        except FileNotFoundError:
            # Nếu file không tồn tại, khởi tạo DataFrame trống
            self.books = pd.DataFrame(columns=['ID', 'Tên sách', 'Tác giả'])

    # Lưu dữ liệu xuống file CSV sau khi thay đổi
    def save_to_file(self):
        self.books.to_csv('books.csv', index=False)

    # Hiển thị danh sách sách
    def display_books(self):
        print(self.books)

    # Tìm kiếm sách sử dụng regex
    def search_books(self, keyword):
        pattern = re.compile(keyword, re.IGNORECASE)
        results = self.books[self.books['Tên sách'].str.contains(pattern)]
        print(results)

    # Thêm sách mới
    def add_book(self):
        new_id = input("Nhập ID sách: ")
        title = input("Nhập tên sách: ")
        author = input("Nhập tên tác giả: ")
        new_book = {'ID': new_id, 'Tên sách': title, 'Tác giả': author}
        self.books = self.books.append(new_book, ignore_index=True)
        self.save_to_file()
        print("Sách đã được thêm thành công!")

    # Cập nhật thông tin sách
    def update_book(self):
        book_id = input("Nhập ID sách để cập nhật: ")
        if book_id in self.books['ID'].values:
            new_title = input("Nhập tên sách mới: ")
            new_author = input("Nhập tên tác giả mới: ")
            self.books.loc[self.books['ID'] == book_id, ['Tên sách', 'Tác giả']] = [new_title, new_author]
            self.save_to_file()
            print("Cập nhật thành công!")
        else:
            print("ID sách không tồn tại!")

    # Xóa sách
    def delete_book(self):
        book_id = input("Nhập ID sách để xóa: ")
        if book_id in self.books['ID'].values:
            self.books = self.books[self.books['ID'] != book_id]
            self.save_to_file()
            print("Xóa sách thành công!")
        else:
            print("ID sách không tồn tại!")

    # Tìm kiếm sách theo tác giả
    def search_by_author(self, author):
        results = self.books[self.books['Tác giả'].str.contains(author, case=False)]
        print(results)

    # Đếm tổng số sách
    def count_books(self):
        print(f"Tổng số sách hiện có: {len(self.books)}")

    # Xuất danh sách sách ra file CSV
    def export_to_csv(self):
        self.books.to_csv('book_list.csv', index=False)
        print("Xuất dữ liệu ra file book_list.csv thành công!")

    # Hiển thị sách theo ID
    def display_book_by_id(self, book_id):
        result = self.books[self.books['ID'] == book_id]
        print(result)
