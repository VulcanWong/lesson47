from abc import ABC, abstractmethod
class Shape(ABC):
    def move(self):
        pass

class square(Shape):
    def move(self):
        print("i am a square i have four sides i am parallel to each other")


class rectangle(Shape):
    def move(self):
        print("i am a rectangle i have longer lines then square")

R = square()
R.move()

K = rectangle()
K.move()