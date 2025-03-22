import tkinter as tk

class ProductListScreen:
    def __init__(self, root, controller):
        self.frame = tk.Frame(root, bg="#ffffff")  
        self.controller = controller

        tk.Label(self.frame, text="Chọn điện thoại", font=("Helvetica", 24, "bold"), bg="#ffffff", fg="#333").pack(pady=10)

        self.list_frame = tk.Frame(self.frame, bg="#ffffff")
        self.list_frame.pack(pady=10)

        button_width = 15  
        button_height = 2
        
        tk.Button(self.frame, text="Quay lại", font=("Arial", 14), bg="#007bff", fg="white",
                  relief="flat", width=button_width, height=button_height, 
                  command=self.controller.show_categories).pack(pady=10)
        
        cart_button = tk.Button(self.frame, text="Giỏ hàng", font=("Arial", 14), bg="#28a745", fg="white",
                                relief="flat", width=button_width, height=button_height, 
                                command=self.controller.show_cart)
        cart_button.pack(pady=5)

    def update_products(self, products):
        """Cập nhật danh sách sản phẩm"""
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        row, col = 0, 0
        button_width = 12  
        button_height = 2

        for product in products:
            frame = tk.Frame(self.list_frame, bg="white", bd=2, relief="solid")
            frame.grid(row=row, column=col, padx=10, pady=10)

            # Hiển thị ảnh nhỏ
            image = self.controller.get_phone_image(product["name"])
            img_label = tk.Label(frame, image=image, bg="white")
            img_label.image = image
            img_label.pack()

            tk.Label(frame, text=product["name"], font=("Arial", 14, "bold"), bg="white").pack(pady=5)

            
            tk.Button(frame, text="Thông tin chi tiết", font=("Arial", 12), bg="#17a2b8", fg="white",
                      relief="flat", width=button_width, height=button_height, 
                      command=lambda pid=product["id"]: self.controller.show_product_detail(pid)).pack(pady=5)

    def pack(self):
        self.frame.pack(fill="both", expand=True)

    def forget(self):
        self.frame.pack_forget()
