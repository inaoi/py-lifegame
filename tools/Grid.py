class Grid:

    def __init__(self, rowCount, colCount):
        self._rowCount = rowCount
        self._colCount = colCount
        self._cells = range(0, colCount * rowCount)

    @property
    def rowCount(self):
        return self._rowCount
        
    @property
    def colCount(self):
        return self._colCount

    def getMoorNeighborhood(self, x, y):
        rowCount = self._rowCount
        colCount = self._colCount
        vRange = range(max(y - 1, 0), min(y + 2, rowCount))
        hRange = range(max(x - 1, 0), min(x + 2, colCount))

        cells = self._cells
        val = []
        for i in vRange:
            vIndex = i * colCount
            index = vIndex + hRange[0]
            val[len(val):] = self._slice(index, len(hRange))

        return val

    def copy(self):
        grid = Grid(self._rowCount, self._colCount)
        origCells = self._cells
        grid._cells = [val for val in origCells]

        return grid

    def _slice(self, index, count):
        return self._cells[index:index + count]


if __name__ == "__main__":
    grid = Grid(5, 5)
    cells = grid.getMoorNeighborhood(4, 4)
    print(cells)
    print(grid.copy()._cells)