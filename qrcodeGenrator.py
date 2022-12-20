import qrcode

from PIL import Image
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=12,border=4)
qr.add_data("https://github.com/AbhishekTwari")
qr.make(fit=True)
img = qr.make_image()
img.save("qrImage.png")
