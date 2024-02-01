from PIL import Image
import pytesseract

# Đọc ảnh từ đường dẫn file
image_path = 'path/to/your/image.png'
image = Image.open(image_path)

# Sử dụng Tesseract OCR để trích xuất văn bản
text = pytesseract.image_to_string(image)

# In văn bản
print(text)
