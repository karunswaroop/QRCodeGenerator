import qrcode

# Define the URL
url = "https://www.youtube.com/@HappyLittleLeadersPlayschool"

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # size of the QR Code (1 = 21x21)
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,  # size of each box in pixels
    border=4,     # border size in boxes
)

qr.add_data(url)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qr_code.png")

print("QR code saved as 'qr_code.png'")

