import os
import pandas as pd
import qrcode

# Load the CSV file
csv_file = 'input.csv'
data = pd.read_csv(csv_file)

# Create the 'QR' folder if it doesn't exist
output_dir = 'QR'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to generate and save the QR code
def create_qr_code(client_id, url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(os.path.join(output_dir, f"{client_id}.jpg"))

# Iterate through the CSV data and generate QR codes
for index, row in data.iterrows():
    client_id = row['client_id']
    url = row['url']
    create_qr_code(client_id, url)

print("QR codes have been generated and saved in the 'QR' folder.")
