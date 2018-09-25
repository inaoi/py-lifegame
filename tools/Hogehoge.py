class Hogehoge:
    
    @staticmethod
    def birth(cells):
        if cells[5]:
            return False

        return cells.count(True) == 3

    @staticmethod
    def alive(cells):
        if not cell[5]:
            return False
            
        lives = cells.count(true)
        return (lives == 2 or lives == 3)
    
    @staticmethod
    def dead(cells):
        if not cells[5]:
            return False

        lives = cells.count(true)
        return (lives <= 1 or 4 <= lives)