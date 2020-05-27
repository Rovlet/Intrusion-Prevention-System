import text_operations
import solution
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyEventHandler(FileSystemEventHandler):
    def __init__(self, path, file_name):
        self.file_name = file_name
        self.path = path
        self.observer = Observer()
        self.text_operations = text_operations.TextOperations(file_name)
        self.solution = solution.Solution()

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(self.file_name):
            self.text_operations.write_new_alert()

    def observe(self):
        self.observer.schedule(self, self.path, recursive=False)
        self.observer.start()
        try:
            while self.observer.is_alive():
                self.observer.join(1)
        except KeyboardInterrupt:
            self.observer.stop()
            print('Bye!')


if __name__ == "__main__":
    handler = MyEventHandler('.', 'alerts')
    handler.observe()
