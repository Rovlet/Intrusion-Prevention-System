from event_handler import EventHandler
from settings import *

if __name__ == "__main__":
    handler = EventHandler('.', ALERT_FILE)
    handler.observe()
