
from pyzbar.pyzbar import decode
from PIL import Image

file="QR.png"
deco=decode(Image.open(file))

print(deco)