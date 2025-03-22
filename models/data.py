from pymongo import MongoClient
import os
from PIL import Image, ImageTk

# Kết nối MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['phone_store']
collection = db['feedback']

# Danh sách danh mục điện thoại
categories = [
    {"id": 1, "name": "iPhone"},
    {"id": 2, "name": "Samsung"},
    {"id": 3, "name": "Xiaomi"},
    {"id": 4, "name": "Huawei"},
    {"id": 5, "name": "LG"},
]

# Danh sách điện thoại
phones = [
    {"id": 1, "categoryId": 1, "name": "iPhone 15 Pro", "price": "$999", "specs": "6.1 inch, A17 Bionic, 48MP camera"},
    {"id": 2, "categoryId": 2, "name": "Samsung S23 Ultra", "price": "$1199", "specs": "6.8 inch, Snapdragon 8 Gen 2, 200MP camera"},
    {"id": 3, "categoryId": 3, "name": "Xiaomi mi 13", "price": "$1020", "specs": "6.6 inch, Snapdragon 8 Gen 1, 200MP camera"},
    {"id": 4, "categoryId": 4, "name": "Huawei Pura 70", "price": "$1000", "specs": "6.2 inch, Snapdragon 8 Gen 2, 250MP camera"},
    {"id": 5, "categoryId": 5, "name": "LG Velvet 5G", "price": "$850", "specs": "6.6 inch, Snapdragon 8 Gen 2, 300MP camera"},
]

# Lưu đánh giá vào MongoDB
def save_feedback(phone_name, feedback_text):
    feedback_data = {"phoneName": phone_name, "feedback": feedback_text}
    collection.insert_one(feedback_data)

# Lấy danh sách đánh giá từ MongoDB
def get_feedbacks(phone_name):
    return list(collection.find({"phoneName": phone_name}))

# Lấy ảnh ngẫu nhiên của sản phẩm
def get_phone_image(phone_name):
    filename = phone_name.lower().replace(" ", "_") + ".jpeg"
    image_path = os.path.join("images", filename)

    print(f"DEBUG: Đang tìm ảnh tại {image_path}")  # Kiểm tra đường dẫn

    try:
        img = Image.open(image_path).resize((200, 200), Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy ảnh {image_path}")  
        return None
