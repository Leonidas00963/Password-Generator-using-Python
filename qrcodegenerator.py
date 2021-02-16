import qrcode

#qr = qrcode.make('Hello World')
#qr.save('myQR.png')

qr = qrcode.QRCode(

    version = 15,
    box_size=15,
    border=5
)

data = 'https://www.webfeinschliff.de/wp-content/uploads/2017/06/karrieretutor-dozent-daniel-werner-1024x1024.png'
qr.add_data(data)
qr.make(fit=true)
img = qr.make_image(fill='black', back_color='white')
img.save('Karriretutor Logo')