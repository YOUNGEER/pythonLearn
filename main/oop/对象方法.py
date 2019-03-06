
class Person():
    def eat(self):
        print(self)

    @classmethod
    def play(cls):
        print(cls)

    @staticmethod
    def say():
        print("Saying")


p = Person()
p.eat()
p.play()
p.say()

Person.play()
Person.say()
# Person.eat()