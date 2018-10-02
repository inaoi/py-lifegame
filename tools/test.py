import threading
import Grid

counter = 0
grid = Grid.Grid(10, 10, lambda x, y: 1)

def task():
    grid.draw()

    t=threading.Timer(1, task)
    t.start()

t=threading.Thread(target = task)
t.start()