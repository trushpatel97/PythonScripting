import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Trush Patel'
email['to'] = 'trushpatel1997@gmail.com'
email['subject'] = 'Sent from python!'

email.set_content('This is the content under the subject')
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login(#your email , #your password)
	smtp.send_message(email)
	print("done")
