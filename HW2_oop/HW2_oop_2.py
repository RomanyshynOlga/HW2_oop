class Person:
    def __init__(self):
        arm_left = Arm('left arm')
        arm_right = Arm('right arm')
        self.arm = [arm_left.human, arm_right.human]


class Arm:
    def __init__(self, human):
        self.human = human


man = Person()
print(man.arm)







class CellPhone:
    def __init__(self, screen):
        self.screen = screen

    def info(self):
        print(f'My new phone has {self.screen}.')


class Screen:
    def __init__(self, function):
        self.function = function


phone = Screen('screen')
phone1 = CellPhone(phone.function)
phone1.info()

