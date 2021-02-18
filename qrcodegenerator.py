
import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR code
s = "Enter your Link or Text Here"

# Generate QR code
url = pyqrcode.create(s)


url.svg("myqr.svg", scale = 8)


url.png('myqr.png', scale = 6)
