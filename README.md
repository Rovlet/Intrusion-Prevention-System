# PyIPS

Intrusion prevention system based on snort alerts.

## How does it work?

Our aplication is still under development. For now it can read snort alerts in the prepared file and is able to make definied action based on snort alert's sid number. 
Definied actions are:

- block source IP address
- block source IP address after 5 alerts within 2 minutes
- do nothing with the alert

When the app is being closed, it sends email to admin with informations about every blocked IP during the day, it also check iptables file for duplicates and too old rules.

### TODO

- [x] Check if app is working well using snort simulation script.
- [x] Check if app is working well using virtual machines and generate real attacks.
- [ ] Make errors handlers with exceptions.
- [ ] Change snort output and app input to not use the same file.


### Prerequisites

To run this program, you need linux, snort, iptables and python3 with watchdog module.

```
sudo apt-get install snort
sudo apt-get install python3
pip3 install watchdog
```


## Team

> Our Contributors

| <a href="" target="_blank">**Rovlet**</a> | <a href="" target="_blank">**kaneron676**</a> | 
| :---: |:---:| 
| [![Rovlet](https://avatars2.githubusercontent.com/u/47760464?s=460&u=3c7215203da5648ec13648db2f78e67c334a14a4&v=4)](github.com/Rovlet)    | [![kaneron676](https://awodev.com/images/default-forum-user.png)](github.com/kaneron676) | [![]()]()  |
| <a href="https://github.com/Rovlet" target="_blank">`github.com/Rovlet`</a> | <a href="https://github.com/kaneron676" target="_blank">`github.com/kaneron676`</a> |
