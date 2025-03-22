import tkinter as tk
from tkinter import messagebox

class ProductDetailScreen:
    def __init__(self, root, controller):
        self.frame = tk.Frame(root, bg="#f8f9fa")
        self.controller = controller

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        self.name_label = tk.Label(self.frame, text="", font=("Helvetica", 24, "bold"), bg="#f8f9fa", fg="#333")
        self.name_label.grid(row=0, column=0, columnspan=2, pady=20, sticky="nsew")

        self.image_label = tk.Label(self.frame, bg="white")
        self.image_label.grid(row=1, column=0, columnspan=2, pady=10, sticky="nsew")

        self.price_label = tk.Label(self.frame, text="", font=("Arial", 18, "bold"), fg="#ff5733", bg="#f8f9fa")
        self.price_label.grid(row=2, column=0, columnspan=2, pady=5, sticky="nsew")

        self.specs_label = tk.Label(self.frame, text="", font=("Arial", 14), wraplength=500, justify="center", bg="#f8f9fa")
        self.specs_label.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

        back_button = tk.Button(self.frame, text="Quay lại", font=("Arial", 14), bg="#007bff", fg="white",
                                relief="flat", padx=15, pady=5, command=lambda: self.controller.show_products(self.controller.current_category_id))
        back_button.grid(row=4, column=0, padx=10, pady=15, sticky="e")

        buy_button = tk.Button(self.frame, text="Mua", font=("Arial", 14), bg="#28a745", fg="white",
                               relief="flat", padx=20, pady=5, command=self.buy_product)
        buy_button.grid(row=4, column=1, padx=10, pady=15, sticky="w")
        
        cart_button = tk.Button(self.frame, text="Giỏ hàng", font=("Arial", 14), bg="#17a2b8", fg="white",
                                relief="flat", padx=15, pady=5, command=self.controller.show_cart)
        cart_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.current_product = None  # Lưu sản phẩm hiện tại để thêm vào giỏ hàng

    def update_product(self, product):
        """Cập nhật giao diện chi tiết sản phẩm"""
        self.current_product = product  # Lưu sản phẩm hiện tại
        self.name_label.config(text=product["name"])
        self.price_label.config(text="Price: " + product["price"])
        self.specs_label.config(text="Specs: " + product["specs"])

        image = self.controller.get_phone_image(product["name"])
        if image:
            self.image_label.config(image=image)
            self.image_label.image = image
        else:
            self.image_label.config(text="Không có ảnh", fg="red")

    def buy_product(self):
        """Thêm sản phẩm vào giỏ hàng và hiển thị giỏ hàng"""
        if self.current_product:
            self.controller.add_to_cart(self.current_product)
            messagebox.showinfo("Giỏ hàng", f"{self.current_product['name']} đã được thêm vào giỏ hàng!")
            self.controller.show_cart()
