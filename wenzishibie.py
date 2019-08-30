from PIL import Image
import pytesseract
text=pytesseract.image_to_string(Image.open('denggao.jpeg'),lang='chi_sim')
print(text)