from Observers import BinaryObserver, HexaObserver, OctalObserver
from Subject import Subject

if __name__ == "__main__":
    subject = Subject()
    BinaryObserver(subject)
    HexaObserver(subject)
    OctalObserver(subject)
    subject.set_state(10)
    subject.set_state(8)
    subject.set_state(15)
