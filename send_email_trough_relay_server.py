import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


# Sending email using relay server without attachment
def send_emails(to_email, date, morning_or_evening, formatted_email_body, branch_or_offsite):
    # from_email = 'novuscc2@outlook.com'
    from_email = 'novushelpdesk@novuslk.com'
    cc_email = 'darshana.gunasekara@novustech.com.sg'
    # cc_email = 'contactcenter2@novustech.com.sg'
    to_email = 'madukapw@yahoo.com'
    # To_email = '; '.join(to_email)
    print(to_email)

    email_subject = 'Subject'

    email_body = "Email Body"

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Cc"] = cc_email
    msg["Subject"] = email_subject
    msg.attach(MIMEText(email_body, "plain"))

    # SMTP server
    smtp_server = "10.200.1.51"
    smtp_port = 25

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.sendmail(from_email, [to_email, cc_email], msg.as_string())
            print(f"Email sent to {to_email}")
            print(email_body)
            time.sleep(2)

    except Exception as e:
        print(f'An error occurred: {e}')


# Sending email using relay server with attachment
def send_emails_with_attachment(output_zip_file, terminal_id, formatted_date, transaction):
    email_from = "from_email"
    email_to = "to_email"
    subject = "Subject"
    body = "Body"

    smtp_server = "10.200.1.51"
    smtp_port = 25

    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    # msg['Cc'] = ", ".join(cc_email_list)
    msg['Subject'] = subject

    # Attach the body of the message
    msg.attach(MIMEText(body, 'plain'))

    # Define the file to attach and open the file as a binary
    attachment = open(output_zip_file, 'rb')

    # Encode as base 64
    attachment_package = MIMEBase('application', 'octet-stream')
    attachment_package.set_payload((attachment).read())
    encoders.encode_base64(attachment_package)
    attachment_package.add_header('Content-Disposition', f'attachment; \
    filename="{os.path.basename(output_zip_file)}"')
    msg.attach(attachment_package)

    # Connect to the SMTP server and send the email with attachment
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # if use_tls:
            #     server.starttls()

            # No login credentials provided for anonymous access
            server.sendmail(email_from, email_to, msg.as_string())
            print("Email with attachment sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        attachment.close()
