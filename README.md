# PyIPS

Intrusion prevention system based on snort alerts.

## How does it work?

Our application is still under development. For now, it can read snort alerts in the prepared file and is able to make defined actions based on snort alert's sid number. 
Defined actions are:

- block the source IP address
- block the source IP address after 5 alerts within 2 minutes
- do nothing with the alert

When the app is being closed, it sends an email to the admin with information about every blocked IP during the day, it also checks iptables file for duplicates and too old rules.

### TODO

- [x] Check if the app is working well using the snort simulation script.
- [x] Check if the app is working well using virtual machines and generate real attacks.
- [ ] Make errors handlers with exceptions.
- [ ] Change snort output and app input to not use the same file.


### Prerequisites

To run this program, you need linux, snort, iptables, and python3 with watchdog module.

1. Install all needed packages
    ```
    sudo apt-get install snort
    sudo apt-get install python3
    pip3 install watchdog
    ```

2. Configure snort to run on your interface and in your network. You can do this in the initialization scripts or by change settings.
3. Change settings.py file:
Path to snort/suricata file
```
    ALERT_FILE = ''
```
If you want to send an email to the admin with program results, you can set receiver and sender data here:
```    
    # Send email to
    ADMIN_EMAIL = ''
    
    # Send email from
    IPS_EMAIL = ''
    IPS_EMAIL_PASSWORD = ''
    
    # Send email from this port
    APPLICATION_PORT = 465
```

You can specify the filename to store temporary iptables rules. This setting is necessary if you want to delete old rules automatically. 
```
    # File to store new rules
    IPTABLES_FILE = 'iptables'
```
After you set this time, the app will check and delete old firewall rules after this time.
```
    # After this time, some periodic actions will occur
    PERIODIC_ACTION_TIME = 60
    
```
## Team

> Our Contributors

| <a href="" target="_blank">**Rovlet**</a> | <a href="" target="_blank">**kaneron676**</a> | 
| :---: |:---:| 
| [![Rovlet](https://avatars2.githubusercontent.com/u/47760464?s=460&u=3c7215203da5648ec13648db2f78e67c334a14a4&v=4)](github.com/Rovlet)    | [![kaneron676](https://awodev.com/images/default-forum-user.png)](github.com/kaneron676) | [![]()]()  |
| <a href="https://github.com/Rovlet" target="_blank">`github.com/Rovlet`</a> | <a href="https://github.com/kaneron676" target="_blank">`github.com/kaneron676`</a> |
