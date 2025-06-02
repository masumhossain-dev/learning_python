import qrcode

def generate_qr_code(filepath, output_path):
    with open(filepath, "r") as file:
        lines = file.readlines()

        text = lines[0].strip()
        filename = lines[1].strip()

        output_path_folder = output_path + '/' + filename
    
    image_QR = qrcode.make(text)
    image_QR.save(output_path_folder)
    print(f"QR code generated and saved as {filename}")

generate_qr_code("read_files/url.txt", "QR_outputs")
