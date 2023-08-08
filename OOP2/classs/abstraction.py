#abstract

from abc import ABC,abstractmethod

class shape(ABC):  # abstract base class
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
    @abstractmethod
    def area(self):  # abstract ke inherit korle must absmethod use korte hobe
        pass

class rectangle(shape):
    def area(self):   # overriding
        print(f'Rectangle area: {self.l * self.w}')

s = rectangle(4,5)
s.area()
# s = shape()