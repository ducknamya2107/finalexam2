import json
import os

class Publishers:
    def __init__(self):
        self.file_path = "publishers.json"
        self.load_publishers()

    def load_publishers(self):
        """Load publishers from the JSON file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                self.publishers = json.load(f)
        else:
            self.publishers = []

    def save_publishers(self):
        """Save publishers to the JSON file."""
        with open(self.file_path, 'w') as f:
            json.dump(self.publishers, f)

    def display_publishers(self):
        """Display the list of publishers."""
        if not self.publishers:
            print("Không có nhà xuất bản nào trong danh sách.")
            return
        print("Danh sách nhà xuất bản:")
        for idx, publisher in enumerate(self.publishers, 1):
            print(f"{idx}. {publisher}")

    def add_publisher(self):
        """Add a new publisher."""
        publisher_name = input("Nhập tên nhà xuất bản: ")
        self.publishers.append(publisher_name)
        self.save_publishers()
        print("Nhà xuất bản đã được thêm thành công.")

    def update_publisher(self):
        """Update an existing publisher."""
        self.display_publishers()
        index = int(input("Nhập số nhà xuất bản muốn cập nhật: ")) - 1
        if 0 <= index < len(self.publishers):
            new_name = input("Nhập tên nhà xuất bản mới: ")
            self.publishers[index] = new_name
            self.save_publishers()
            print("Nhà xuất bản đã được cập nhật thành công.")
        else:
            print("Số nhà xuất bản không hợp lệ.")

    def delete_publisher(self):
        """Delete a publisher."""
        self.display_publishers()
        index = int(input("Nhập số nhà xuất bản muốn xóa: ")) - 1
        if 0 <= index < len(self.publishers):
            self.publishers.pop(index)
            self.save_publishers()
            print("Nhà xuất bản đã được xóa thành công.")
        else:
            print("Số nhà xuất bản không hợp lệ.")
