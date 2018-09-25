import Hogehoge

class World():
    def __init__(self):
        self.grid = grid = [[1] * 5] * 5

    def printLines(self):
        for line in self.grid[1:-1]:
            print(line)
        

world = World()
world.printLines()

print(Hogehoge.Hogehoge.isBorn([1, 1, 1, 0, 0, 0, 0, 0, 0]))