# coding: UTF-8

class Viewer:
    
    @staticmethod
    def draw(cells, colCount):
        index = 0
        for row in grid:
            outputData = ""
            for cell in row:
                outputData += "■" if cell else " "

            print outputData