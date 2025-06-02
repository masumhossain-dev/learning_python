import qrcode

text = input("Enter yout text or link to convert into QR code: ")
filename = input("Enter your saved file name: ")

def generate_qr_code(text, filename):
    image_QR = qrcode.make(text)

    image_QR.save(filename)

generate_qr_code(text, filename)
    
    

