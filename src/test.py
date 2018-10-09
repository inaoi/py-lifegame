import threading
import random
import board
import Hogehoge
import viewer


counter = 0
world = board.Board(50, 50, lambda x, y: random.randrange(0, 2))
viewer = viewer.Viewer()
automaton = Hogehoge.Automaton()


def task():
    viewer.draw(world)

    for y in range(0, world.rowCount):
        for x in range(0, world.colCount):

            moor = world.getMoorNeighborhood(x, y)

            result = 0
            if automaton.birth(moor) or automaton.alive(moor):
                result = 1
            else:
                result = 0

            world.setValue(x, y, result)
    world.commit()

    t = threading.Timer(1, task)
    t.start()


t = threading.Thread(target=task)
t.start()
