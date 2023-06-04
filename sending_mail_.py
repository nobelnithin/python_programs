'''import smtplib
from email.message import EmailMessage

email=EmailMessage()
email['from']="Noblenithin"
email["to"]="msdrahuljohn@gmail.com"
email['subject']='hi hshhs'

email.set_content('nithin noithh')
with smtplib.SMTP(host='smtp.gmail.com',port=578) as smpt:
    smtp.ehlo()
    smtp.starttls()'''

import smtplib
