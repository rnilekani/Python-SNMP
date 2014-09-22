'''
This script shows how to send emails via Python.
'''

def send_mail(recipient, subject, message, sender):
    '''
    Simple function to help simplify sending SMTP email

    Assumes a mailserver is available on localhost
    '''

    import smtplib
    from email.mime.text import MIMEText

    message = MIMEText(message)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient

    # Create SMTP connection object to localhost
    smtp_conn = smtplib.SMTP('localhost')

    # Send the email
    smtp_conn.sendmail(sender, recipient, message.as_string())

    # Close SMTP connection

    smtp_conn.quit()

    return True


if __name__ == '__main__':
	
	recipient = 'nilekani.raunaq@gmail.com'
	subject = 'Test message'
	message = '''
  This is a fictional message

Regards,
Ron
'''	
