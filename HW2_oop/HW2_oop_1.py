class Animals:
    def __init__(self, name, eat, sleep):
        self.name = name
        self.eat = eat
        self.sleep = sleep

    def print_animals(self):
        print(f'I am a {self.name} i love to {self.eat} and {self.sleep}.')

class Animal1_Cat(Animals):
    def __init__(self, name, eat, sleep, sound):
        super().__init__(name, eat, sleep)
        self.sound = sound

    def print_sound(self):
        print(f'and say {self.sound}')


class Animal2_Dog(Animals):
    def __init__(self, name, eat, sleep, status):
        super().__init__(name, eat, sleep)
        self.status = status


    def print_status(self):
        print(f'I am {self.status}')

class Animal3_Mouse(Animals):
    def __init__(self, name, eat, sleep, do):
        super().__init__(name, eat, sleep)
        self.do = do


    def print_do(self):
        print(f'I like to {self.do}')


class Animal4_Cow(Animals):
    def __init__(self, name, eat, sleep, friend):
        super().__init__(name, eat, sleep)
        self.friend = friend

    def print_friend(self):
        print(f'I am friends with a {self.friend}.')


class Animal5_Goat(Animal4_Cow):
    def __init__(self, name, eat, sleep, friend, size):
        super().__init__(name, eat, sleep, friend)
        self.size = size

    def print_size(self):
        print(f'I am {self.size} in size')


class Human:
   def __init__(self, eat, sleep, study, work):
       self.eat = eat
       self.sleep = sleep
       self.study = study
       self.work = work

   def print_human(self):
       print(f'After a {self.sleep}  ,I  {self.eat} and go {self.study} or {self.work}.')

class Centaur(Human, Animals):
    def __init__(self,name, eat, sleep, study, work,vacation):
        Human.__init__(self, eat, sleep, study, work)
        Animals.__init__(self, name, eat, sleep)
        self.vacation =vacation

    def print_vacation(self):
        print(f'I have {self.vacation} vacation.')

centaur=Centaur('Ron','eat sandwich','long sleep','study','work','long')
centaur.print_human()
centaur.print_animals()
centaur.print_vacation()
print(issubclass(Centaur, Animals))


anim1 = Animal1_Cat('cat', 'eat meet', 'more sleep', '"Meow"')
anim1.print_animals()
anim1.print_sound()
print(issubclass(Animal1_Cat, Animals))
anim2 = Animal2_Dog('dog', 'eat meet', 'more sleep', 'Boss')
anim2.print_animals()
anim2.print_status()
print(issubclass(Animal2_Dog, Animals))
anim3 = Animal3_Mouse('mouse', 'eat cheese', 'more sleep', 'run')
anim3.print_animals()
anim3.print_do()
print(issubclass(Animal3_Mouse, Animals))
anim4 = Animal4_Cow('cow', 'eat grass', 'get some sleep', 'goat')
anim4.print_animals()
anim4.print_friend()
print(issubclass(Animal4_Cow, Animals))
anim5 = Animal5_Goat('goat', 'eat tree leaves', 'get some sleep', 'cow', 'little')
anim5.print_animals()
anim5.print_size()
anim5.print_friend()
print(issubclass(Animal5_Goat, Animals))