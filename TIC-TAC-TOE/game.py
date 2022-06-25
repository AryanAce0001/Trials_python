class TIcTacToe:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]    # we will use a single list to represent 3x3 board
        self.current_winner= None   #keeps track of the winner 
    
    def print_board(self):
        for row :