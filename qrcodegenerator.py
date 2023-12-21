import qrcode





def generate_qrcode(url): 
    qr = qrcode.QRCode(
    version = 15,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 5
)



    qr.add_data(url)

    qr.make(fit = True)

    img = qr.make_image(fill = "black", back_color = "white")
    img.save("myqrcimage.png")


url = input("Enter URL: ")
generate_qrcode(url)