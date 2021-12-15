# Machine IP
MACHINE_IP = ''

# Send email to
ADMIN_EMAIL = ''

# Send email from
IPS_EMAIL = ''
IPS_EMAIL_PASSWORD = ''

# File to storenew rules
IPTABLES_FILE = 'iptables'

# After this time, some periodic actions will occur
PERIODIC_ACTION_TIME = 60

# Send email from this port
APPLICATION_PORT = 465

HOSTILE_NETWORK_EVENTS = {
    "Pinging": False,
    "Nmap XMAS Tree Scan": True,
    "Possible SSH brute forcing": False,
    "Nmap FIN Scan": False,
    "FTP Potential Brute Force Attack": False,
}
