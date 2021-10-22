from datetime import date, datetime
import re
import defense_machine


class Alerts:
    def __init__(self, file_name):
        self.solution = defense_machine.DefenseMachine()
        self.file_name = file_name
        self.alert_file = open(self.file_name, 'r')
        self.alert_file.seek(0, 2)
        self.high_sid_alert_number = 100000
        self.alert_message = ''
        self.ips_report_name = 'IPS_report_' + date.today().strftime('%d_%m_%y') + '.txt'

    def handle_new_alert(self):
        ips_report = open(self.ips_report_name, 'a+')
        next_line = self.alert_file.readline()
        if next_line.strip():
            blocked_address, sid = self.find_snort_alert(next_line)
            if blocked_address:
                message = "{} IP {} was blocked! Snort sid: {} \n".format(datetime.now().time(), blocked_address, sid)
                ips_report.write(message)
                return message
        ips_report.close()
        return 0

    def find_snort_alert(self, line):
        m = re.match(r"([0-9:./-]+)\s+.*?\[[0-9]\:([0-9]+)\:+.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})+.*?\s+->\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)
        sid = int(m.group(2))
        if sid > self.high_sid_alert_number:
            operation = self.solution.block_address_after_number_of_attempts(m.group(3))
        else:
            operation = self.solution.block_address(m.group(3))
        return [operation, sid]
