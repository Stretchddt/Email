import os
import smtplib
from email.message import EmailMessage
import imghdr

email = os.environ.get('BUS_MAIL')
password = os.environ.get('BUS_PASS')

contacts = ['edplus90@gmail.com', 'thomsontkd1@gmail.com', 'stretchddt@yahoo.com']

msg = EmailMessage()
msg['Subject'] = 'Hey, check out these photos'
msg['From'] = email
msg['To'] = ', '.join(contacts)
msg.set_content('Images below!')

attachments = ['photo1.jpg', 'photo2.jpg', 'photo3.jpg', 'photo4.jpg',]

for a in attachments:
    with open(a, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

        msg.add_attachment(file_data, maintype='image', subtype='file_type', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as test:

    test.login(email, password)

    test.send_message(msg)