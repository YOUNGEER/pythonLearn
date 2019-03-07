


def say(self):
    print("saying")

def talk(self):
    print("talking")

A = type('AName',(object,),{'class_say':say,'class_talk':talk})

a=A()
a.class_say()
a.class_talk()