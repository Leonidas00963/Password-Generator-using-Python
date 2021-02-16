import qrcode



qr = qrcode.QrCode(
    version=1,
    box_size=15,
    border=5
)

data = 'https://www.webfeinschliff.de/wp-content/uploads/2017/06/karrieretutor-dozent-daniel-werner-1024x1024.png'
qr.add_data(data)
qr.make(ƒit=true)
img = qr.make_image(ƒill='black', back_color='white')
img.save('Karriretutor Logo.png')