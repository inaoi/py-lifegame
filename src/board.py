import ListHelper


class Board:

    _listHelper = ListHelper.ListHelper()

    def __init__(self, rowCount, colCount, initFunc):
        self._rowCount = rowCount
        self._colCount = colCount
        self._cells = [initFunc(x, y) for y in range(0, colCount)
                       for x in range(0, rowCount)]
        self._buff = [self._cells[i] for i in range(0, len(self._cells))]

    @property
    def rowCount(self):
        return self._rowCount

    @property
    def colCount(self):
        return self._colCount

    def setValue(self, x, y, value):
        self._buff[y * self._colCount + x] = value

    def getValue(self, x, y):
        return self._cells[y * self._colCount + x]

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
            rowCells = self._listHelper._slice(cells, index, len(hRange))

            self._listHelper._fill(rowCells, 3, 0, x == 0)

            val[len(val):] = rowCells

        self._listHelper._fill(val, 9, 0, y == 0)

        return val

    def commit(self):
        self._cells = self._buff
        self._buff = [self._cells[i] for i in range(0, len(self._cells))]
