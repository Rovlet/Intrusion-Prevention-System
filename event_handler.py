from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import alerts
import defense_machine
import periodic_actions


class EventHandler(FileSystemEventHandler):
    def __init__(self, path, alert_file):
        self.file_name = alert_file
        self.path = path
        self.observer = Observer()
        self.text_operations = alerts.Alerts(self.file_name)
        self.solution = defense_machine.DefenseMachine()
        self.periodic_actions = periodic_actions.PeriodicActions()
        self.today_events = []

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(self.file_name):
            new_event = self.text_operations.handle_new_alert()
            if new_event:
                self.today_events.append(new_event)

    def observe(self):
        self.observer.schedule(self, self.path, recursive=False)
        self.observer.start()
        try:
            while self.observer.is_alive():
                self.observer.join(1)
        except KeyboardInterrupt:
            self.observer.stop()
            self.periodic_actions.delete_old_rules_from_firewall()
            self.periodic_actions.send_email_to_admin(self.today_events)
