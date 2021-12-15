from datetime import date, datetime
import defense_machine


class HandleAlerts:
    def __init__(self):
        self.defense = defense_machine.DefenseMachine()
        self.ips_report_name = 'IPS_report_' + date.today().strftime('%d_%m_%y') + '.txt'

    def handle_new_alert(self, alert_message, address, block_now=False):
        with open(self.ips_report_name, 'a+') as ips_report:
            if block_now:
                message = "{} IP address {} was blocked. Message: {} \n".format(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), address, alert_message)
                ips_report.write(message)
                self.defense.block_address(address)
                return message
            else:
                self.defense.block_address_after_number_of_attempts(address)
