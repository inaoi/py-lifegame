import Hogehoge
import Viewer

class Fugafuga:

    def __init__(self):
        self._cells = [[1] * 25]
        self._colCount = 5
        self._grid = grid = [[True] * 5] * 5
        self._automaton = Hogehoge.Automaton()
        self._viewer = Viewer.Viewer()

    def nextGeneration(self):
        arr = self._getRegion(1, 2)
        if self._automaton.birth(arr) or self._automaton.alive():
            return True
        elif self._automaton.dead(arr):
            return False

        return False

        
    
    @staticmethod
    def _getMoorNeighborhood(x, y, grid):
        return [0, 0, 0, 0, 0, 0, 0, 0, 0]

    

    def _getRegion(self, x, y):
        return [1, 1, 1, 0, 0, 0, 0, 0, 0]

    def printGrid(self):
        self._viewer.draw(self._grid)
        

fugafuga = Fugafuga()
print(fugafuga.nextGeneration())
fugafuga.printGrid()
        