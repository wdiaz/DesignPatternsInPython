class Subject:
    def __init__(self):
        self.observers = []
        self.state = 0;

    def set_state(self, state):
        self.state = state
        self.notify()

    def notify(self):
        """ send signals to every registered observer."""
        for observer in self.observers:
            observer.update()

    def attach(self, observer):
        self.observers.append(observer)