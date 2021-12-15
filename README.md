# Intrusion Prevention System v2.0

Intrusion prevention system connected with Snort by the Ryu app. 
This app is only working in the Linux environment with running Snort.

## How does it work?
When Snort will find something in our network that may be hostile, 
it sends all alerts to the Ryu app which is our Intrusion Prevention System. 
If the IPS detects any alerts messages defined in the settings file:
```
HOSTILE_NETWORK_EVENTS = {
    "Pinging": False,
    "Nmap XMAS Tree Scan": True,
    "Possible SSH brute forcing": False,
    "Nmap FIN Scan": False,
    "FTP Potential Brute Force Attack": False,
}
```

it will decide to block the host immediately (True), or to count the packet and if it is above a threshold (False), it will block the host.
For some hostile traffic, we can define the threshold of packets to block the host.

We can also enable email notifications to be sent to the administrator by the App. 
To do this, we need to change the below configuration in the file settings.py:
```
ADMIN_EMAIL = ''
IPS_EMAIL = ''
IPS_EMAIL_PASSWORD = ''
APPLICATION_PORT =''
```
When the configuration is set, the application will be sending information about the detected hostile traffic after a defined time.
It will also include a report about the blocked hosts.

### How to start

To run this program, you need to have Linux, Python3, Ryu, Snort, and Iptables installed.
```
sudo apt-get snort
```
Make sure you set the right interface and network when Snort was being installed.
If Snort is working fine, you should be able to write this command without any error:
```
snort - i <your interface> -A unsock -l /tmp -c /etc/snort/snort.conf
```

Then, you need to install other dependencies:
```
sudo apt install python3 python3-pip ryu iptables
sudo apt install gcc python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev zlib1g-dev
```

Every .py file in this repository needs to be installed with Ryu, otherwise, imports will not work.
To add every file to Ryu, you need to run this command:
```
sudo ryu-manager --app-lists *.py
```
You need to start with these files, which don't have any relative imports, otherwise, you will get an error. For example, defense_machine.py doesn't have any relative imports, so you can start with that file.

After that, you can start the application by running the event_handler app:
```
sudo ryu-manager event_handler.py
```
Also, make sure that Snort is running, otherwise, the app won't get any alerts.

## Team

> Our Contributors

| <a href="" target="_blank">**Rovlet**</a> | <a href="" target="_blank">**kaneron676**</a> | 
| :---: |:---:| 
| [![Rovlet](https://avatars2.githubusercontent.com/u/47760464?s=460&u=3c7215203da5648ec13648db2f78e67c334a14a4&v=4)](github.com/Rovlet)    | [![kaneron676](https://awodev.com/images/default-forum-user.png)](github.com/kaneron676) | [![]()]()  |
| <a href="https://github.com/Rovlet" target="_blank">`github.com/Rovlet`</a> | <a href="https://github.com/kaneron676" target="_blank">`github.com/kaneron676`</a> |
