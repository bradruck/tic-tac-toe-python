# Tic-Tac-Toe

class TicTacToe(object):
    def __init__(self):
        self.available_players = ['X', 'O']
        self.squares = ['L1', 'C1', 'R1', 'L2', 'C2', 'R2', 'L3', 'C3', 'R3']
        self.valid_value = [1, 10]
        self.grid_layout = 'L1\t\tC1\t\tR1\nL2\t\tC2\t\tR2\nL3\t\tC3\t\tR3\n'
        self.map_values = {'X': 1, 'O': 10}
        self.print_values = {1: 'X', 10: 'O', 0: '-'}
        self.game_status = {'L1': 0, 'C1': 0, 'R1': 0,
                            'L2': 0, 'C2': 0, 'R2': 0,
                            'L3': 0, 'C3': 0, 'R3': 0}
        self.mapped_entry = 0
        self.player = ''
        self.loc = ''
        self.RED = "\033[0;91m"
        self.GREEN = "\033[0;92m"
        self.BLUE = "\033[0;94m"
        self.YELLOW = "\033[0;93m"
        self.PURPLE = "\033[0;95m"
        self.WHITE = "\033[0;97m"

    # Initial function to launch a game
    #
    def begin_game(self):
        print(self.WHITE + '\nWelcome to a friendly game of Tic-Tac-Toe,')
        # request initial play to choose X or O
        self.choose_initial_player()
        self.choose_square()

    # Request player choice for initial move
    #
    def choose_initial_player(self):
        self.player = input('Please choose which player you wish to be, \'X\' or \'O\':  ').upper()
        while self.player not in self.available_players:
            self.player = input('That was not a valid entry, please enter either \'X\' or \'O\':  ').upper()

    # Alternate the players automatically
    #
    def alternate_player(self):
        if self.player == 'X':
            return 'O'
        return 'X'

    # Primary function to interact with players
    #
    def choose_square(self):
        # display board layout and prompt player to choose square and make entry
        if self.player == "X":
            print('\nYour turn ' + self.BLUE + '\'{}\''.format(self.player), end='')
        else:
            print('\nYour turn ' + self.YELLOW + '\'{}\''.format(self.player), end='')
        print(self.WHITE + ', here is the board lay-out for choosing a square to play:\n{}'.format(self.grid_layout))
        self.loc = input('Please enter the desired location of your move:  ').upper()
        while self.loc not in self.squares:
            self.loc = input('That was not a valid location, please re-enter the desired location:  ').upper()
        self.mapped_entry = self.map_values.get(self.player)
        self.validate_entry()

    # Evaluate the entry for validity and square availability, loop back to choose_square() to continue turns
    #
    def validate_entry(self):
        # check to see if chosen square is already taken
        if self.game_status.get(self.loc) not in self.valid_value:
            self.game_status[self.loc] = self.mapped_entry
            # evaluate puzzle based on new entry
            self.evaluate_game()
            self.print_current_board()
        else:
            print('That square has been taken, please re-enter a new square.')
            print('\nHere is the current board:')
            self.print_current_board()
            self.choose_square()
        self.player = self.alternate_player()
        self.choose_square()

    # Evaluate game to determine if there is a winner, if not check if game is still in progress or a tie
    #
    def evaluate_game(self):
        if self.evaluate_win_scenarios():
            print(self.GREEN + '\nYou win {}!!'.format(self.player))
        else:
            # see if there are any open squares left, else game has resulted in a tie
            if any(x == 0 for x in self.game_status.values()):
                print('\nHere is the current board:')
                return
            else:
                print(self.PURPLE + '\nTie game!' + self.WHITE)
        self.exit_game()

    # Evaluate the various row, column or diagonal win possibilities
    #
    def evaluate_win_scenarios(self):
        if (self.game_status.get('L1') + self.game_status.get('C1') + self.game_status.get('R1')) == 3 or \
                (self.game_status.get('L1') + self.game_status.get('C1') + self.game_status.get('R1')) == 30:
            return True
        elif (self.game_status.get('L2') + self.game_status.get('C2') + self.game_status.get('R2')) == 3 or \
                (self.game_status.get('L2') + self.game_status.get('C2') + self.game_status.get('R2')) == 30:
            return True
        elif (self.game_status.get('L3') + self.game_status.get('C3') + self.game_status.get('R3')) == 3 or \
                (self.game_status.get('L3') + self.game_status.get('C3') + self.game_status.get('R3')) == 30:
            return True
        elif (self.game_status.get('L1') + self.game_status.get('L2') + self.game_status.get('L3')) == 3 or \
                (self.game_status.get('L1') + self.game_status.get('L2') + self.game_status.get('L3')) == 30:
            return True
        elif (self.game_status.get('C1') + self.game_status.get('C2') + self.game_status.get('C3')) == 3 or \
                (self.game_status.get('C1') + self.game_status.get('C2') + self.game_status.get('C3')) == 30:
            return True
        elif (self.game_status.get('R1') + self.game_status.get('R2') + self.game_status.get('R3')) == 3 or \
                (self.game_status.get('R1') + self.game_status.get('R2') + self.game_status.get('R3')) == 30:
            return True
        elif (self.game_status.get('L1') + self.game_status.get('C2') + self.game_status.get('R3')) == 3 or \
                (self.game_status.get('L1') + self.game_status.get('C2') + self.game_status.get('R3')) == 30:
            return True
        elif (self.game_status.get('L3') + self.game_status.get('C2') + self.game_status.get('R1')) == 3 or \
                (self.game_status.get('L3') + self.game_status.get('C2') + self.game_status.get('R1')) == 30:
            return True
        else:
            return False

    # Print the current state of the game board
    #
    def print_current_board(self):
        n = 0
        for y in range(3):
            for x in list(self.game_status)[n:n+3]:
                board_value = self.print_values.get(self.game_status[x])
                if board_value == "X":
                    print(self.BLUE + board_value, '\t\t', end='')
                elif board_value == "O":
                    print(self.YELLOW + board_value, '\t\t', end='')
                else:
                    print(self.WHITE + board_value, '\t\t', end='')
                n += 1
            print(self.WHITE)

    # Print final result and exit
    #
    def exit_game(self):
        print(self.WHITE + '\nHere is the final board:')
        self.print_current_board()
        print(self.RED + "\nThank-you for playing!")
        exit(0)


if __name__ == '__main__':
    play = TicTacToe()
    play.begin_game()
