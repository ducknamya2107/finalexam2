import json
class Request_manager:
    @staticmethod
    def choose_action():
        print("Chọn hành động cho phiếu mượn sách.")
        # Logic để xử lý hành động

class Book_loan_requests:
    
    def __init__(self):
        self.file_path = 'requests.json'
        self.requests = self.load_requests()

    def load_requests(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_requests(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.requests, file)

    def display_requests(self):
        if not self.requests:
            print("Không có phiếu mượn trong hệ thống.")
        else:
            for request in self.requests:
                print(request)

    def add_request(self):
        new_request = {
            'customer_name': input("Nhập tên khách hàng: "),
            'book_title': input("Nhập tiêu đề sách: "),
            'loan_date': input("Nhập ngày mượn: "),
            'return_date': input("Nhập ngày trả: ")
        }
        self.requests.append(new_request)
        self.save_requests()
        print("Phiếu mượn đã được thêm thành công.")

    def update_request(self):
        customer_name = input("Nhập tên khách hàng cần cập nhật phiếu mượn: ")
        for request in self.requests:
            if request['customer_name'] == customer_name:
                request['book_title'] = input("Nhập tiêu đề sách mới: ")
                request['loan_date'] = input("Nhập ngày mượn mới: ")
                request['return_date'] = input("Nhập ngày trả mới: ")
                self.save_requests()
                print("Phiếu mượn đã được cập nhật.")
                return
        print("Không tìm thấy phiếu mượn.")

    def delete_request(self):
        customer_name = input("Nhập tên khách hàng cần xóa phiếu mượn: ")
        self.requests = [request for request in self.requests if request['customer_name'] != customer_name]
        self.save_requests()
        print("Phiếu mượn đã được xóa.")
