import pyqrcode
import png

link = input("Input the URL\n")
qr_code = pyqrcode.create(link)
qr_code.png("link.png", scale=5)
