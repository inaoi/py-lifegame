import threading
import random
import Grid
import Hogehoge

counter = 0
grid = Grid.Grid(30, 20, lambda x, y: random.randrange(0, 2))
automaton = Hogehoge.Automaton()

def task():
    grid.draw()

    for y in range(0, grid.rowCount):
        for x in range(0, grid.colCount):

            moor = grid.getMoorNeighborhood(x, y)

            result = 0
            if automaton.birth(moor) or automaton.alive(moor):
                result = 1
            else:
                result = 0

            grid.setValue(x, y, result)
    grid.commit()

    t=threading.Timer(1, task)
    t.start()

t=threading.Thread(target = task)
t.start()