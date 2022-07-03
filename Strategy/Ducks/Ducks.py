from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self) -> None:
        """ Defined in child classes"""
        pass


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self) -> None:
        """Defined in the child classes"""
        pass


class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print("Yoo, I'm flying")


class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print("I can't fly")


class MuteQuack(QuackBehavior):
    @abstractmethod
    def quack(self) -> None:
        print("I can't Quack")


class Quack(QuackBehavior):
    def quack(self) -> None:
        print('Quack')


class Squeak(QuackBehavior):
    def quack(self) -> None:
        print('Squeak')


class Duck(ABC):

    def __init__(self, quackbehavior: QuackBehavior, flybehavior: FlyBehavior):
        self.quackBehavior = quackbehavior
        self.flyBehavior = flybehavior

    def executeQuack(self):
        self.quackBehavior.quack()

    def executeFly(self):
        self.flyBehavior.fly()

    @abstractmethod
    def whoiam(self) -> None:
        pass


class MallardDuck(Duck):

    def __init__(self, quackBehavior: QuackBehavior, flyBehavior: FlyBehavior):
        super().__init__(quackBehavior, flyBehavior)

    def whoiam(self) -> None:
        print('I am a Mallard Duck')


class RubberDuck(Duck):
    def __init__(self, quackBehavior: QuackBehavior, flyBehavior:FlyBehavior):
        super().__init__(quackBehavior,flyBehavior)

    def whoiam(self) -> None:
        print('I am a rubber duck')


duck = MallardDuck(Quack(), FlyWithWings())
duck.executeQuack()
duck.executeFly()
duck.whoiam()


duck = RubberDuck(Squeak(), FlyNoWay())
duck.executeQuack()
duck.executeFly()
duck.whoiam()

