import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "superbased20@gmail.com"
password = "rvsc pxbi hbqq fyyy"

receiver_email = "nika@mziuri.ge"
msg = MIMEText("hello icl ts is a testing msg")
msg['subject'] = 'Smtp Test'
msg['from'] = sender_email
msg['to'] = receiver_email

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print('email sent succesfully')


def send_email_with_attachment():
    subject = "Email with Attachment"
    body = "nigger attachment"
    
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    filename = "nigger.txt"
    attachment = open(filename, "rb")

    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {filename}")

    msg.attach(part)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("attachment sent successfully")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        attachment.close()
        server.quit()


send_email_with_attachment()