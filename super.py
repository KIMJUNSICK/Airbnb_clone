class Dog:
    def __init__(self):
        print("woof woof")

    def pee(self):
        print("peeeee")


class Puppy(Dog):
    def pee(self):
        print("I'm pupee, not pee")
        super().pee()


wal = Puppy()

wal.pee()
