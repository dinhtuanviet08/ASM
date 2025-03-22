import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os

class HomeScreen:
    def __init__(self, root, controller):
        self.frame = tk.Frame(root, bg="#f0f8ff") 
        self.controller = controller

        # Tiêu đề chính
        tk.Label(self.frame, text="Chào mừng đến với cửa hàng", font=("Helvetica", 28, "bold"), bg="#f0f8ff", fg="#333").pack(pady=20)

        # Ảnh logo
        image_path = os.path.join(os.path.dirname(__file__), "..", "images", "store_logo.png")

        # Mở ảnh bằng PIL
        original_image = Image.open(image_path)
        resized_image = original_image.resize((200, 200), Image.LANCZOS)  # Resize ảnh nếu cần
        self.logo = ImageTk.PhotoImage(resized_image)  # Chuyển đổi ảnh để dùng với Tkinter

        # Hiển thị logo trong Label
        logo_label = tk.Label(self.frame, image=self.logo, bg="#f0f8ff")
        logo_label.pack(pady=10)

        # Nút vào danh mục
        browse_button = tk.Button(self.frame, text="Tham khảo sản phẩm", font=("Arial", 16, "bold"),
                                  bg="#007bff", fg="white", relief="flat", padx=20, pady=10,
                                  command=self.controller.show_categories)
        browse_button.pack(pady=15)

        cart_button = tk.Button(self.frame, text="Giỏ hàng", font=("Arial", 14), bg="#28a745", fg="white",
                                relief="flat", padx=15, pady=5, command=self.controller.show_cart)
        cart_button.pack(pady=10)

    def pack(self):
        self.frame.pack(fill="both", expand=True)

    def forget(self):
        self.frame.pack_forget()
