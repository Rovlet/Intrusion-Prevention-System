import smtplib
import ssl
import os.path
import subprocess
import re
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email_content import text_email, html_email
from report import save_report
from settings import *
from datetime import datetime, date


class PeriodicActions:
    def __init__(self):
        self.port = APPLICATION_PORT
        self.ips_email_address = IPS_EMAIL
        self.admin_email = ADMIN_EMAIL
        self.iptables_file = IPTABLES_FILE
        self.periodic_actions_time = PERIODIC_ACTION_TIME

    def delete_old_rules_from_firewall(self):
        pass
        subprocess.check_output('iptables-save > iptables', shell=True)
        if os.path.exists(self.iptables_file):
            lines_seen = []
            outfile = open('iptables-copy', "w+")
            for line in open(self.iptables_file, "r"):
                if line not in lines_seen:
                    if "comment" in line:
                        creation_time = re.findall(r"\"(1[1-9].*?)\"", line)
                        if time.time() - float(creation_time[0]) < self.periodic_actions_time:
                            outfile.write(line)
                            lines_seen.append(line)
                    else:
                        outfile.write(line)
                        lines_seen.append(line)
                else:
                    if "COMMIT" in line:
                        lines_seen = []
                        outfile.write(line)
                        lines_seen.append(line)
            outfile.close()
        subprocess.check_output('iptables-restore < iptables-copy', shell=True)

    def add_report_as_attachment(self, message, list_of_events):
        save_report(list_of_events)
        now = datetime.now()
        attachmentPath = 'Report of today\'s events %s.pdf' % (now.strftime("%d-%m-%Y"))
        try:
            with open(attachmentPath, "rb") as attachment:
                p = MIMEApplication(attachment.read(), _subtype="pdf")
                p.add_header('Content-Disposition', "attachment; filename= %s" % attachmentPath.split("\\")[-1])
                message.attach(p)
        except Exception as e:
            print(str(e))
        return message

    def send_email_to_admin(self, list_of_events):
        password = IPS_EMAIL_PASSWORD
        message = MIMEMultipart("alternative")
        message["Subject"] = "IPS raport {}".format(date.today().strftime('%d_%m_%y'))
        message["From"] = self.ips_email_address
        message["To"] = self.admin_email
        events = "\n".join(list_of_events)
        plain_email = MIMEText(text_email.format(events), "plain")
        events = "<br>".join(list_of_events)
        email_with_html = MIMEText(html_email.format(events), "html")

        message = self.add_report_as_attachment(message, list_of_events)

        message.attach(plain_email)
        message.attach(email_with_html)
        make_context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=make_context) as server:
            server.login(self.ips_email_address, password)
            server.sendmail(
                self.ips_email_address, self.admin_email, message.as_string()
            )
