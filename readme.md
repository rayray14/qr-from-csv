# QR Code Generator from CSV
This Python script reads a CSV file containing Client ID and URL information and generates QR codes as JPG images for each entry. The generated QR codes are saved in a folder named `QR`.


## Dependencies
- pandas
- qrcode

To install the required packages, use the following command:
pip install -r requirements.txt


## Usage
Update the csv_file variable in the generate_qr_codes.py script with the path to your CSV file.

Run the Python script:
python generate.py

The QR codes will be generated and saved as JPG images in the QR folder, with the filenames being the respective Client IDs.


## CSV Format
The CSV file should have two columns: Client ID and URL. Here's an example of the CSV format:
Client ID,URL
123,https://example.com/123
456,https://example.com/456
789,https://example.com/789
