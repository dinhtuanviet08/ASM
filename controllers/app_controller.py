from models.data import categories, phones, save_feedback, get_feedbacks, get_phone_image
from views.home_screen import HomeScreen
from views.category_screen import CategoryScreen
from views.product_list import ProductListScreen
from views.product_detail import ProductDetailScreen
from views.cart_screen import CartScreen


class AppController:
    def __init__(self, root):
        self.root = root  
        self.root.title("Phone Store")  
        self.root.geometry("1000x800")  
        self.root.configure(bg="#f0f0f0")  

        self.current_category_id = None  
        self.current_product_id = None  
        self.cart = []  # Giỏ hàng

        # Khởi tạo các màn hình
        self.home_screen = HomeScreen(root, self)
        self.category_screen = CategoryScreen(root, self)
        self.product_list_screen = ProductListScreen(root, self)
        self.product_detail_screen = ProductDetailScreen(root, self)
        self.cart_screen = CartScreen(root, self)  

        self.show_home()  # Hiển thị màn hình chính đầu tiên

    def show_frame(self, frame):
        """Ẩn tất cả màn hình khác và chỉ hiển thị màn hình được chọn"""
        for f in (
            self.home_screen.frame,
            self.category_screen.frame,
            self.product_list_screen.frame,
            self.product_detail_screen.frame,
        ):
            f.pack_forget()
        frame.pack(fill="both", expand=True)

    def get_categories(self):
        """Lấy danh sách hãng điện thoại"""
        return categories

    def get_products_by_category(self, category_id):
        """Lọc danh sách điện thoại theo hãng"""
        return [p for p in phones if p["categoryId"] == category_id]

    def get_product_by_id(self, product_id):
        """Lấy thông tin sản phẩm theo ID"""
        return next(p for p in phones if p["id"] == product_id)

    def get_phone_image(self, phone_name):
        """Lấy ảnh của điện thoại"""
        return get_phone_image(phone_name)

    def save_feedback(self, phone_name, feedback_text):
        """Lưu đánh giá vào MongoDB"""
        save_feedback(phone_name, feedback_text)

    def get_feedbacks(self, phone_name):
        """Lấy danh sách đánh giá từ MongoDB"""
        return get_feedbacks(phone_name)

    def show_home(self):
        """Hiển thị màn hình chính"""
        self.show_frame(self.home_screen.frame)

    def show_categories(self):
        """Hiển thị danh sách hãng điện thoại"""
        self.show_frame(self.category_screen.frame)

    def show_products(self, category_id):
        """Hiển thị danh sách sản phẩm theo hãng"""
        self.current_category_id = category_id
        products = self.get_products_by_category(category_id)
        self.product_list_screen.update_products(products)
        self.show_frame(self.product_list_screen.frame)

    def show_product_detail(self, product_id):
        """Hiển thị chi tiết sản phẩm"""
        self.current_product_id = product_id
        product = self.get_product_by_id(product_id)
        self.product_detail_screen.update_product(product)
        self.show_frame(self.product_detail_screen.frame)
        
    def add_to_cart(self, product):
        """Thêm sản phẩm vào giỏ hàng"""
        self.cart.append(product)
        self.cart_screen.update_cart(self.cart)

    def remove_from_cart(self, product):
        """Xóa sản phẩm khỏi giỏ hàng"""
        self.cart.remove(product)
        self.cart_screen.update_cart(self.cart)

    def clear_cart(self):
        """Xóa toàn bộ giỏ hàng sau khi thanh toán"""
        self.cart.clear()
        self.cart_screen.update_cart(self.cart)

    def show_cart(self):
        """Hiển thị màn hình giỏ hàng và lưu màn hình trước đó"""
        self.cart_screen.previous_screen = self.get_current_screen()  # Lưu màn hình hiện tại
        self.show_frame(self.cart_screen.frame)


    def get_current_screen(self):
        """Trả về màn hình hiện tại"""
        if self.product_detail_screen.frame.winfo_ismapped():
            return self.product_detail_screen.frame
        elif self.product_list_screen.frame.winfo_ismapped():
            return self.product_list_screen.frame
        elif self.category_screen.frame.winfo_ismapped():
            return self.category_screen.frame
        return self.home_screen.frame  

