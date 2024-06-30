import qrcode

modify_images_QR = qrcode.QRCode(version=1, box_size=40, border=4)
modify_images_QR.add_data(f"Name: AdewebsTEchologies\n Purpose: This is a sample project\n Contact Info:08131116906\n Facebook: https://facebook.com/adewebs1")
modify_images_QR.make(fit=True)
OutputImage = modify_images_QR.make_image(fill_color="black", back_color= "white")
OutputImage.save("securityCard.png")
