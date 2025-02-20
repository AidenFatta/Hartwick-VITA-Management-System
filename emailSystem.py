import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_Expiring_Email(cert_name, expiration_date, user_email):
    msg = MIMEMultipart()
    msg['FROM'] = 'INSERT EMAIL HERE'
    msg['TO'] = user_email
    msg['SUBJECT'] = 'Reminder for expiring experience!'
    message = f'This is a reminder that your experience "{cert_name}" will expire on {expiration_date}'
    msg.attach(MIMEText(message))

    if expiration_date != "":
        mailserver = smtplib.SMTP('smtp.gmail.com',587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login('INSERT EMAIL HERE', 'INSERT EMAIL APP PASSWORD HERE')
        mailserver.sendmail('INSERT EMAIL HERE', user_email, msg.as_string())
        mailserver.quit()
    else:
        print("Failure: Experience doesn't expire")

def send_Opportunity_Email(cert_name, user_email):
    msg = MIMEMultipart()
    msg['FROM'] = 'INSERT EMAIL HERE'
    msg['TO'] = user_email
    msg['SUBJECT'] = 'Upcoming Experience Opportunity!'
    message = f'This is a alert that there is an upcoming experience opporutunity: "{cert_name}"'
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('INSERT EMAIL HERE', 'INSERT EMAIL APP PASSWORD HERE')
    mailserver.sendmail('INSERT EMAIL HERE', user_email, msg.as_string())
    mailserver.quit()