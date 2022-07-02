from Observer import Observer
from Subject import Subject


class BinaryObserver(Observer):
    def __init__(self, subject: Subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self) -> None:
        print(f"Value {self.subject.state} in binary is: {bin(self.subject.state)} ")


class HexaObserver(Observer):
    def __init__(self, subject: Subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self) -> None:
        print(f"Value {self.subject.state} in hexadecimal is: {hex(self.subject.state)}")


class OctalObserver(Observer):
    def __init__(self, subject: Subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self) -> None:
        print(f"Value {self.subject.state} in octal is: {oct(self.subject.state)}")
