from abc import abstractmethod, ABC

class LaptopInterface:
    @abstractmethod
    def screen(self):
        raise NotImplementedError('This method was not implemented')
    @abstractmethod
    def keyboard(self):
        raise NotImplementedError('This method was not implemented')
    @abstractmethod
    def touchpad(self):
        raise NotImplementedError('This method was not implemented')
    @abstractmethod
    def webcam(self):
        raise NotImplementedError('This method was not implemented')
    @abstractmethod
    def ports(self):
        raise NotImplementedError('This method was not implemented')
    @abstractmethod
    def dynamics(self):
        raise NotImplementedError('This method was not implemented')

class HPLaptop(LaptopInterface):
    def screen(self):
        print('My laptop has a screen.')
    def keyboard(self):
        print('My laptop has a keyboard.')
    def touchpad(self):
        print('My laptop has a touchpad.')
    def webcam(self):
        print('My laptop has a webcam.')
    def ports(self):
        print('My laptop has a ports.')
    def dynamics(self):
        print('My laptop has dynamics.')

myleptop=HPLaptop()
myleptop.screen()
myleptop.keyboard()
myleptop.touchpad()
myleptop.webcam()
myleptop.ports()
myleptop.dynamics()





