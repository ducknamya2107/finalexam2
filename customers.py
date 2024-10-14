import json

class Customers:
    def __init__(self):
        self.file_path = 'customers.json'
        self.customers = self.load_customers()

    def load_customers(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_customers(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.customers, file)

    def display_customers(self):
        if not self.customers:
            print("Không có khách hàng trong hệ thống.")
        else:
            for customer in self.customers:
                print(customer)

    def add_customer(self):
        new_customer = {
            'name': input("Nhập tên khách hàng: "),
            'email': input("Nhập email: "),
            'phone': input("Nhập số điện thoại: ")
        }
        self.customers.append(new_customer)
        self.save_customers()
        print("Khách hàng mới đã được thêm.")

    def update_customer(self):
        name = input("Nhập tên khách hàng cần cập nhật: ")
        for customer in self.customers:
            if customer['name'] == name:
                customer['email'] = input("Nhập email mới: ")
                customer['phone'] = input("Nhập số điện thoại mới: ")
                self.save_customers()
                print("Thông tin khách hàng đã được cập nhật.")
                return
        print("Không tìm thấy khách hàng.")

    def delete_customer(self):
        name = input("Nhập tên khách hàng cần xóa: ")
        self.customers = [customer for customer in self.customers if customer['name'] != name]
        self.save_customers()
        print("Khách hàng đã được xóa.")
