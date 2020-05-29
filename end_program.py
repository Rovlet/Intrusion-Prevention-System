import smtplib
import ssl
import os.path
import subprocess
import re 
import time
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EndProgram:
    def __init__(self):
        self.port = 465
        self.ips_email_address = ""
        self.admin_email = ""
        self.iptables_file = 'iptables'
        self.two_weeks = 60

    def check_firewall(self):
        subprocess.check_output('iptables-save > iptables', shell=True)
        if os.path.exists(self.iptables_file):
            lines_seen = []
            outfile = open('iptables-copy', "w+")
            for line in open(self.iptables_file, "r"):
                if line not in lines_seen:
                    if "comment" in line:
                       m = re.findall(r"\"(1[1-9].*?)\"", line)
                       if time.time() - float(m[0]) < self.two_weeks:
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

    def make_email_message(self, list_of_events):
        password = input("Type your password and press enter:")
        message = MIMEMultipart("alternative")
        message["Subject"] = "IPS raport {}".format(date.today().strftime('%d_%m_%y'))
        message["From"] = self.ips_email_address
        message["To"] = self.admin_email
        events = "\n".join(list_of_events)
        # plain-text
        text = """\
        Hi! 
        List of today's events:
        {}
        Have a nice day!""".format(events)
        events = "<br>".join(list_of_events)
        # html code
        html = """\
        <html>
          <body style ="font-family: Arial, Helvetica, sans-serif; text-align: center; 
          background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(138,61,81,1) 35%, rgba(0,212,255,1) 100%);
          padding: 3%; max-width: 600px;">
          <div style = "position: relative; display:grid; background: rgba(255,255,255,0.94);
    border-radius: 5px; box-shadow: 0px 0px 11px -1px rgba(46,46,46,1); width: 600px;">
           <h2 style=" padding:40px; font-weight:lighter; text-transform:uppercase; color:#414141;"
            >Hi admin</h2>
            <p>List of today's events:<br> </p>
            <p>
               {}
            </p>
            <p style="padding:40px;">Have a nice day!</p>
            <br>
            </div>
          </body>
        </html>
        """.format(events)
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        make_context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=make_context) as server:
            server.login(self.ips_email_address, password)
            server.sendmail(
                self.ips_email_address, self.admin_email, message.as_string()
            )
