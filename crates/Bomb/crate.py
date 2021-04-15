from crates.Default.crate import Crate

class BombCrate(Crate):

    def __init__(self, pygame, row, num):
        super(BombCrate, self).__init__(pygame, row, num, "crates/images/Bomb.png")
    
    def hitByBall(self):
        super().hitByBall()
        for crate in Crate.Crates:
            if abs(self.row - crate.row) == 1 and abs(self.col - crate.col) == 1:
                crate.hitByBall()
        # cratesInRangeRow = [row for row in [self.row - 1, self.row, self.row + 1] if not row < 0 and not row > 2]
        # cratesInRangeCol = [col for col in [self.col - 1, self.col, self.col + 1] if not col < 0 and not col > 9]

        
        