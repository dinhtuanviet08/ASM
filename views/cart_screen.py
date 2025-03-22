import tkinter as tk
from tkinter import messagebox

class CartScreen:
    def __init__(self, root, controller):
        self.frame = tk.Frame(root, bg="#ffffff")
        self.controller = controller
        self.previous_screen = None  # Lưu màn hình trước khi vào giỏ hàng

        tk.Label(self.frame, text="Giỏ hàng", font=("Helvetica", 24, "bold"), bg="#ffffff", fg="#333").pack(pady=10)

        self.cart_list_frame = tk.Frame(self.frame, bg="#ffffff")
        self.cart_list_frame.pack(pady=10)

        self.total_label = tk.Label(self.frame, text="Total: $0", font=("Arial", 16, "bold"), fg="#ff5733", bg="#ffffff")
        self.total_label.pack(pady=10)

        checkout_button = tk.Button(self.frame, text="Thanh toán", font=("Arial", 14), bg="#28a745", fg="white",
                                    relief="flat", padx=20, pady=5, command=self.checkout)
        checkout_button.pack(pady=5)

        self.back_button = tk.Button(self.frame, text="Quay lại", font=("Arial", 14), bg="#007bff", fg="white",
                                     relief="flat", padx=15, pady=5, command=self.go_back)
        self.back_button.pack(pady=5)

    def update_cart(self, cart_items):
        """Cập nhật danh sách sản phẩm trong giỏ hàng"""
        for widget in self.cart_list_frame.winfo_children():
            widget.destroy()

        total_price = 0
        for item in cart_items:
            frame = tk.Frame(self.cart_list_frame, bg="white", bd=1, relief="solid")
            frame.pack(pady=5, fill="x")

            tk.Label(frame, text=item["name"], font=("Arial", 14), bg="white").pack(side="left", padx=10)
            tk.Label(frame, text=item["price"], font=("Arial", 14, "bold"), fg="#ff5733", bg="white").pack(side="left", padx=10)

            remove_button = tk.Button(frame, text="❌ Remove", font=("Arial", 12), bg="#dc3545", fg="white",
                                      relief="flat", command=lambda p=item: self.controller.remove_from_cart(p))
            remove_button.pack(side="right", padx=10)

            total_price += int(item["price"].replace("$", ""))  

        self.total_label.config(text=f"Total: ${total_price}")

    def checkout(self):
        """Xử lý thanh toán"""
        messagebox.showinfo("Thanh toán", "✅ Thanh toán thành công! Cảm ơn bạn.")
        self.controller.clear_cart()

    def go_back(self):
        """Quay lại màn hình trước đó và ẩn giỏ hàng"""
        self.frame.pack_forget()  # Ẩn giỏ hàng
        if self.previous_screen:
            self.controller.show_frame(self.previous_screen)
        else:
            self.controller.show_home()  # Nếu không có màn hình trước, quay về trang chủ
