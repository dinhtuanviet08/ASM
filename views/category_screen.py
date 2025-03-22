import tkinter as tk

class CategoryScreen:
    def __init__(self, root, controller):
        self.frame = tk.Frame(root, bg="#f0f8ff")  
        self.controller = controller

        tk.Label(self.frame, text="Hãy chọn hãng điện thoại bạn muốn mua", font=("Helvetica", 24, "bold"), bg="#f0f8ff", fg="#333").pack(pady=20)

        self.button_frame = tk.Frame(self.frame, bg="#f0f8ff")
        self.button_frame.pack(pady=10)

        colors = ["#ffc107", "#ff5733", "#28a745", "#17a2b8"]  # Màu sắc khác nhau cho từng hãng
        button_width = 15  # Đặt kích thước cố định cho các nút
        button_height = 2

        for index, category in enumerate(self.controller.get_categories()):
            tk.Button(self.button_frame, text=category["name"], font=("Arial", 16, "bold"),
                      bg=colors[index % len(colors)], fg="#fff", relief="flat",
                      width=button_width, height=button_height,
                      command=lambda cid=category["id"]: self.controller.show_products(cid)).pack(pady=10)

        cart_button = tk.Button(self.frame, text="Giỏ hàng", font=("Arial", 14), bg="#28a745", fg="white",
                                relief="flat", width=button_width, height=button_height, 
                                command=self.controller.show_cart)
        cart_button.pack(pady=10)
        
    def pack(self):
        self.frame.pack(fill="both", expand=True)

    def forget(self):
        self.frame.pack_forget()
