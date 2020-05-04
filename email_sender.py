import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Allan Butler'
email['to'] = 'sarabutler92@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'
email.set_content('I love you')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('allanbutler9@gmail.com', 'XXXXX')
    smtp.send_message(email)
    print('all good boss!')
