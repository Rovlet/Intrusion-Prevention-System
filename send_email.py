import smtplib
import ssl
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail:
    def __init__(self):
        self.port = 465
        self.ips_email_address = ""
        self.admin_email = ""

    def make_message(self, list_of_events):
        password = input("Type your password and press enter:")
        message = MIMEMultipart("alternative")
        message["Subject"] = "IPS raport {}".format(date.today().strftime('%d_%m_%y'))
        message["From"] = self.ips_email_address
        message["To"] = self.admin_email
        events = "".join(list_of_events)

        # plain-text
        text = """\
        Hi! 
        List of today's events:
        {}
        Have a nice day!""".format(events)

        part1 = MIMEText(text, "plain")
        # part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        # message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.ips_email_address, password)
            server.sendmail(
                self.ips_email_address, self.admin_email, message.as_string()
            )
