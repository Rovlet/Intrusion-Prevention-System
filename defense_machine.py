import subprocess
from time import time


class DefenseMachine:
    def __init__(self):
        self.att_count = []
        self.blocked_addresses = []

    def block_address(self, source_ip):
        if source_ip in self.blocked_addresses:
            return 0
        p = subprocess.Popen(["iptables", "-t", "filter", "-A", "INPUT", "-d", "{}".format(source_ip), "-m", "comment", "--comment", "{}".format(time()), "-j", "DROP"],
                              stdout=subprocess.PIPE)
        output, err = p.communicate()
        print("Address {} blocked".format(source_ip))
        self.blocked_addresses.append(source_ip)
        return source_ip

    def block_address_after_number_of_attempts(self, source_ip):
        if source_ip in self.blocked_addresses:
            return
        now = time()
        self.att_count = [[a, b, c] for [a, b, c] in self.att_count if now-b < 60]
        for sublist in self.att_count:
            if sublist[0] == source_ip:
                if sublist[2] > 4:
                    return self.block_address(source_ip)
                else:
                    sublist[2] += sublist[2]
                    return 
        self.att_count.append([source_ip, now, 1])
        return
