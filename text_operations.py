from datetime import date
import re
import solution


class TextOperations:
    def __init__(self, file_name):
        self.solution = solution.Solution()
        self.file_name = file_name
        self.alert_file = open(self.file_name, 'r')
        self.alert_file.seek(0, 2)
        self.high_sid_alert_number = 100000
        self.alert_message = ''

    def write_new_alert(self):
        pass
        ips_report_name = 'IPS_report_' + date.today().strftime('%d_%m_%y') + '.txt'
        ips_report = open(ips_report_name, 'a+')
        next_line = self.alert_file.readline()
        if next_line.strip():
            blocked_address, sid = self.find_snort_alert(next_line)
            if blocked_address:
                ips_report.write("IP {} was blocked! Snort sid: {} \n".format(blocked_address, sid))
        ips_report.close()

    def find_snort_alert(self, line):
        m = re.match(r"([0-9:./-]+)\s+.*?\[[0-9]\:([0-9]+)\:+.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s+"
                     r"->\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})", line)
        sid = int(m.group(2))
        if sid < self.high_sid_alert_number:
            self.operation = self.solution.block_after_count(m.group(3))
        else:
            self.operation = self.solution.block_address(m.group(3))
        return [self.operation, sid]
