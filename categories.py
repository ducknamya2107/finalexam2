import json

class Categories:
    def __init__(self):
        self.file_path = 'categories.json'
        self.categories = self.load_categories()

    def load_categories(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_categories(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.categories, file)

    def display_categories(self):
        if not self.categories:
            print("Không có danh mục sách.")
        else:
            for category in self.categories:
                print(category)

    def add_category(self):
        new_category = input("Nhập tên danh mục mới: ")
        self.categories.append(new_category)
        self.save_categories()
        print("Danh mục mới đã được thêm.")

    def update_category(self):
        old_category = input("Nhập tên danh mục cần cập nhật: ")
        if old_category in self.categories:
            new_category = input("Nhập tên danh mục mới: ")
            index = self.categories.index(old_category)
            self.categories[index] = new_category
            self.save_categories()
            print("Danh mục đã được cập nhật.")
        else:
            print("Danh mục không tồn tại.")

    def delete_category(self):
        category = input("Nhập tên danh mục cần xóa: ")
        self.categories = [cat for cat in self.categories if cat != category]
        self.save_categories()
        print("Danh mục đã được xóa.")
