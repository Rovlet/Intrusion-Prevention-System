import os.path
from os import path
from random import uniform
import time


if __name__ == "__main__":
    alert_copy = 'alerts_to_copy'
    alert_paste = '../alerts'
    if path.exists(alert_copy):
        with open(alert_copy, "r") as a_file:
            for line in a_file:
                stripped_line = line.strip()
                with open(alert_paste, "a+") as paste_file:
                    paste_file.write(stripped_line+'\n')
                time.sleep(uniform(0.01, 0.5))
