from picamera import PiCamera
from time import sleep
from gpiozero import Button
from email import encoders
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os

camera = PiCamera()
button = Button(2)
camera.start_preview()
frame = 1
while True:
    try:
        button.wait_for_press()
        camera.capture('/home/pi/My coding/Coding_pic/frame%03d.jpg'% frame)

        fromaddr = "myprojects2828@gmail.com"
        toaddr = "altenjohn12@gmail.com"


        msg = MIMEMultipart()


        msg['From'] = fromaddr


        msg['To'] = toaddr


        msg['Subject'] = "Alert!"


        body = "Someone enter restricted area."


        msg.attach(MIMEText(body, 'plain'))


        filename = 'frame%03d.jpg'%frame
        attachment = open(("/home/pi/My coding/Coding_pic/frame%03d.jpg"%frame), "rb")


        p = MIMEBase('application', 'octet-stream')


        p.set_payload((attachment).read())


        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)


        msg.attach(p)


        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        s.login(fromaddr, "Noblenithin2828")

        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)

        s.quit() 
        
        
        frame += 1
        
    except KeyboardInterrupt:
        camera.stop_preview()
        break