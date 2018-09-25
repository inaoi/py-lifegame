import Hogehoge

class Fugafuga:

    def __init__(self):
        self.hogehoge = Hogehoge.Hogehoge()
        self.abc = 'abc'

    def nextGeneration(self):
        arr = [1, 1, 1, 0, 0, 0, 0, 0, 0]
        if self.hogehoge.birth(arr) or self.hogehoge.alive():
            return True
        elif self.hogehoge.dead(arr):
            return False

        return False
    
    def printABC(self):
        print(self.abc)

fugafuga = Fugafuga()
print(fugafuga.nextGeneration())
        