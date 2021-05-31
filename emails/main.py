import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email_id = 'yamkelapj@gmail.com'
receiver_email_id = ['brentleejohnson73@gmail.com', 'jaydenmay040@gmail.com', 'thapelo@lifechoices.com']
password = input("Password:")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = ", ".join(receiver_email_id)
msg['Subject'] = subject
body = "HI I AM SEDNING YOU AN EMAIL VIA PYCHARM !!\n"
body = body + "Python email tester"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login(sender_email_id, password)

# sending the mail
s.sendmail(sender_email_id, receiver_email_id, text)
# terminating the session
s.quit()
