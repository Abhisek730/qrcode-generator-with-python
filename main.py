# Print a message to indicate that the application has started
print("Application Started")

# Import necessary modules
import qrcode  # Import the qrcode module for generating QR codes
from PIL import Image  # Import the Image module from the Pillow library for image manipulation

# Create an instance of the QRCode class
qr = qrcode.QRCode(
    version=1,  # The version of the QR code (1 to 40, higher means more data)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level (H: High)
    box_size=10,  # Size of each box in the QR code
    border=4,  # Border thickness around the QR code
)

# Add data (in this case, a LinkedIn profile URL) to the QRCode instance
qr.add_data("https://www.linkedin.com/in/abhishek-agrawal-233689245/")

# Generate the QR code with the specified settings
qr.make(fit=True)

# Create an image from the QRCode instance, specifying fill and background colors
img = qr.make_image(fill_color="red", back_color="blue")

# Save the generated QR code image to a file
img.save("sample_qr.png")
