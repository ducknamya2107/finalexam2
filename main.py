from books import Books
from book_loan_requests import Book_loan_requests, Request_manager
from categories import Categories
from customers import Customers
from publishers import Publishers

# Tạo một từ điển chứa các class để tiện tương tác
class_library = {
    "1": Books(),
    "2": Book_loan_requests(),
    "3": Categories(),
    "4": Customers(),
    "5": Publishers()
}

if __name__ == "__main__":
    while True:
        print('-----------Chương Trình Quản Lý Thư Viện------------')
        print('''
            1: Books          4: Customers
            2: Requests       5: Publishers
            3: Categories  ''')
        user_input = input("Nhập mã đối tượng muốn tương tác ('exit' để thoát): ")

        if user_input == 'exit':
            print("Bye")
            break

        if user_input in class_library:
            # Lấy class tương ứng từ dictionary
            selected_class = class_library[user_input]
            
            # Nếu là Books (quản lý sách)
            if user_input == '1':
                print('Quản lý Books:')
                print('1: Hiển thị sách\n2: Thêm sách\n3: Cập nhật sách\n4: Xóa sách\n5: Tìm kiếm sách')
                action = input("Nhập hành động bạn muốn thực hiện: ")
                if action == '1':
                    selected_class.display_books()
                elif action == '2':
                    selected_class.add_book()
                elif action == '3':
                    selected_class.update_book()
                elif action == '4':
                    selected_class.delete_book()
                elif action == '5':
                    keyword = input("Nhập từ khóa để tìm kiếm: ")
                    selected_class.search_books(keyword)
                else:
                    print("Lựa chọn không hợp lệ!")
                    
            # Nếu là Requests (quản lý phiếu mượn sách)
            elif user_input == '2':
                print('Quản lý Requests:')
                print('1: Hiển thị phiếu mượn\n2: Thêm phiếu mượn\n3: Cập nhật phiếu mượn\n4: Xóa phiếu mượn')
                action = input("Nhập hành động bạn muốn thực hiện: ")
                if action == '1':
                    selected_class.display_requests()
                elif action == '2':
                    selected_class.add_request()
                elif action == '3':
                    selected_class.update_request()
                elif action == '4':
                    selected_class.delete_request()
                else:
                    print("Lựa chọn không hợp lệ!")

            # Nếu là Categories (quản lý danh mục sách)
            elif user_input == '3':
                print('Quản lý Categories:')
                print('1: Hiển thị danh mục\n2: Thêm danh mục\n3: Cập nhật danh mục\n4: Xóa danh mục')
                action = input("Nhập hành động bạn muốn thực hiện: ")
                if action == '1':
                    selected_class.display_categories()
                elif action == '2':
                    selected_class.add_category()
                elif action == '3':
                    selected_class.update_category()
                elif action == '4':
                    selected_class.delete_category()
                else:
                    print("Lựa chọn không hợp lệ!")

            # Nếu là Customers (quản lý khách hàng)
            elif user_input == '4':
                print('Quản lý Customers:')
                print('1: Hiển thị khách hàng\n2: Thêm khách hàng\n3: Cập nhật khách hàng\n4: Xóa khách hàng')
                action = input("Nhập hành động bạn muốn thực hiện: ")
                if action == '1':
                    selected_class.display_customers()
                elif action == '2':
                    selected_class.add_customer()
                elif action == '3':
                    selected_class.update_customer()
                elif action == '4':
                    selected_class.delete_customer()
                else:
                    print("Lựa chọn không hợp lệ!")

            # Nếu là Publishers (quản lý nhà xuất bản)
            elif user_input == '5':
                print('Quản lý Publishers:')
                print('1: Hiển thị nhà xuất bản\n2: Thêm nhà xuất bản\n3: Cập nhật nhà xuất bản\n4: Xóa nhà xuất bản')
                action = input("Nhập hành động bạn muốn thực hiện: ")
                if action == '1':
                    selected_class.display_publishers()
                elif action == '2':
                    selected_class.add_publisher()
                elif action == '3':
                    selected_class.update_publisher()
                elif action == '4':
                    selected_class.delete_publisher()
                else:
                    print("Lựa chọn không hợp lệ!")

        else:
            print("Đối tượng không tồn tại. Vui lòng thử lại.")

    print('Thoát chương trình.')
