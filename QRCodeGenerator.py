import qrcode


def main():
    data = input("Enter the URL: ")
    qrcode_filename = input("Enter the QR code filename: ")
    gen_qr_Code(data, qrcode_filename)


def gen_qr_Code(url, qrcode_filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qrcode_filename)


main()
