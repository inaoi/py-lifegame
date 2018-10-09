# coding: UTF-8


class Viewer:

    @staticmethod
    def draw(board):
        colCount = board.colCount
        rowCount = board.rowCount
        rowIndex = 0
        outputData = ""

        for y in range(0, rowCount):
            for x in range(0, colCount):
                outputData += "@" if board.getValue(x, y) == 1 else " "
                if x == colCount - 1:
                    outputData += '\n'

        print outputData
        print "----------------------------"
