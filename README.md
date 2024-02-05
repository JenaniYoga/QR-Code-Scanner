# QR Code Scanner
This Python script, `QR Code Scanner.py`, is designed to scan QR codes from images using the `pyzbar` library. It reads QR codes from an image file specified within the script (`QR.png` in this case), decodes the information, and prints the decoded content.

## Prerequisites
Before running the script, ensure you have the following dependencies installed:
- `pyzbar`: You can install it using pip:
  pip install pyzbar
  
- `PIL` (Python Imaging Library): You can install it using pip:
  pip install pillow
  
## Usage
1. Place the QR code image file you want to scan in the same directory as the script.
2. Update the `file` variable in the script with the filename of your QR code image.
3. Run the script using Python:
   python QR\ Code\ Scanner.py

4. The script will decode the QR code(s) in the image and print the decoded content to the console.

## Note
- Ensure that the QR code image file (`QR.png` by default) is accessible and correctly named.
- This script assumes that there is only one QR code in the image. If there are multiple QR codes, it will decode all of them.
- Make sure that the QR code is clear and well-defined in the image to ensure accurate decoding.
  
Feel free to customize and modify the script according to your requirements!
