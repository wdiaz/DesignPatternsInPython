from Ducks import MallardDuck, Quack, FlyWithWings


def test_MallardDuckQuack(capsys):
    duck = MallardDuck(Quack(), FlyWithWings())
    duck.executeQuack()
    captured = capsys.readouterr()
    assert captured.out == "Quack\n"


def test_MallardDuckFly(capsys):
    duck = MallardDuck(Quack(), FlyWithWings())
    duck.executeFly()
    captured = capsys.readouterr()
    assert captured.out == "Yoo, I'm flying\n"


def test_MallardDuckWhoIs(capsys):
    duck = MallardDuck(Quack(), FlyWithWings())
    duck.whoiam()
    captured = capsys.readouterr()
    assert captured.out == "I am a rubber duck\n"

