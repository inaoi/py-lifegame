# coding: UTF-8

class Viewer:
    
    @staticmethod
    def draw(cells, colCount):
        rowIndex = 0
        outputData = ""

        for i in range(0, len(cells)):
            outputData += "@" if cells[i] == 1 else " "
            if i % colCount == colCount - 1:
                outputData += '\n'

        print outputData