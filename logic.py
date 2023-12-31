import copy

class NoneType: # To set different parts of the game
    def __init__(self): # To initialize objects
        self.colour = -10

    def __repr__(self): # To display the outputs
        return "▢"

    def checker(self, y, x, y1, x1): # xy are the coordinates of our game board and x1y1 are the coordinates of the player
        return False

    def shcan_beat(self, y, x, y1, x1):
        return (False, 0, 0)

    def shcan_move(self, y, x, y1, x1):
        return False


class ChessFigure: # Making a chess board
    IMG = None

    def __init__(self, colour, y=None, x=None):
        self.colour = colour
        self.y = y
        self.x = x

    def __repr__(self):
        return self.IMG[1 if self.colour else 0] # If it is 1, display the image we uploaded, otherwise display the empty house


class Pawn(ChessFigure):
    point = 0

    IMG = ("♙", "♟")

    def checker(self, y, x, y1, x1):
        if self.colour == 1:
            colour_position = 1 # If the color position is 1, it means the color of the bead is black
            y_factor = y1 + 1 # Because the soldier can only move one house forward or down
        else:
            colour_position = -1 # means it is white
            y_factor = y1 - 1
        # if the position entered by the player is outside this range, it will return the wrong result message.    
        if y1 < 0 or y1 > 7: 
            win_current = False
        # if the position entered by the player is outside this range, it will return the wrong result message.     
        elif x1 < 0 or x1 > 7: 
            win_current = False
        else: # If the player enters the correct coordinates
            if t.board[y1][x1].colour == -10: # -10: dot
                if y == 6 or y == 1:
                    if (
                        x == x1
                        and 0 < (y - y1) * colour_position < 3 # Being black or white
                        and t.board[y_factor][x1].colour == -10 # There is an empty house in front of her
                    ):
                        win_current = True
                    elif x == x1 and (y - y1) * colour_position == 1: # There is an empty house in front of her
                        win_current = True
                    else:
                        win_current = False
                else:
                    if x == x1 and (y - y1) * colour_position == 1: # Move the soldier & There is an empty house in front of her
                        win_current = True
                    else:
                        win_current = False
            elif abs(t.board[y1][x1].colour - t.board[y][x].colour) == 1:
                if abs(x - x1) == 1 and (y - y1) * colour_position == 1: # If the house is full
                    win_current = True
                else:
                    win_current = False
            else:
                win_current = False
        return win_current


class King(ChessFigure):
    IMG = ("♔", "♚")

    def checker(self, y, x, y1, x1):
        if abs(x1 - x) == 1 and abs(y1 - y) == 1: # Oblique movement
            win_current = True
        elif abs(x1 - x) == 0 and abs(y1 - y) == 1: # Vertical movement
            win_current = True
        elif abs(x1 - x) == 1 and abs(y1 - y) == 0: # Horizontal movement
            win_current = True
        else: # The houses around the king are full.
            win_current = False

        q = kw if self.colour == 0 else kb  # kw: king white  # kb: King black 
        for i in range(-1, 2): # 1: Move   0: stabile  -1:undo
            for j in range(-1, 2):
                try: # Updates the position of the beads
                    if t.board[y1 + i][x1 + j] == q:
                        win_current = False
                except:
                    continue
        return win_current


class Quinn(ChessFigure):
    IMG = ("♕", "♛")

    def checker(self, y, x, y1, x1):
        q = qb if self.colour == 0 else qw # Color selection

        c = lw if q == qw else lb # Ladya
        v = cw if q == qw else cb # Bishop

        if x == x1 or y == y1: # Direct movement like Ladya
            return c.checker(y, x, y1, x1)
        elif (y != y1 and x != x1) or (x != x1 and y != y1): # Oblique movement like Bishop
            return v.checker(y, x, y1, x1)
        else:
            return False


class Ladya(ChessFigure): 
    IMG = ("♖", "♜")

    def checker(self, y, x, y1, x1):
        win_current = True
        if y == y1 and x != x1: # Moving along the horizon
            q = x if x1 > x else x1 # Determine left and right movement
            e = x1 if x1 > x else x
            for i in t.board[y][q + 1 : e]: # Moving on the horizon and adding value
                if i != dot:
                    win_current = False
        elif x == x1 and y != y1: # Vertical movement
            q = y1 if y > y1 else y  # Determination of up and down movement
            e = y if y > y1 else y1
            for i in t.board[q + 1 : e]:
                if i[x] != dot:
                    win_current = False
        else:
            win_current = False
        return win_current


class Horse(ChessFigure):
    IMG = ("♘", "♞")

    def checker(self, y, x, y1, x1):
        if abs(y - y1) == 2 and abs(x - x1) == 1: # 2 moves up or down and 1 move to the left or right
            win_current = True
        elif abs(x - x1) == 2 and abs(y - y1) == 1: # 2 moves left or right and 1 move up or down
            win_current = True
        else:
            win_current = False # There is no other movement
        return win_current


class Bishop(ChessFigure): 
    IMG = ("♗", "♝")

    def checker(self, y, x, y1, x1):
        win_current = True
        if x == x1 or y == y1: # do not move
            win_current = False
        elif x + y == x1 + y1: # Move diagonally to the right
            q = x1 if x1 > x and y > y1 else x
            c = y1 if x1 > x and y > y1 else y
            v = y if x1 > x and y > y1 else y1
            for i in t.board[c + 1 : v]:
                if i[q - 1] != dot:
                    win_current = False
                q -= 1
        elif x + y1 == y + x1: # Move diagonally to the left
            q = x if x1 > x and y1 > y else x1
            c = y if x1 > x and y1 > y else y1
            v = y1 if x1 > x and y1 > y else y
            for i in t.board[c + 1 : v]:
                if i[q + 1] != dot:
                    win_current = False
                q += 1
        else:
            win_current = False
        return win_current


class LHorse(ChessFigure):
    IMG = ("♖♘", "♜♞")

    def checker(self, y, x, y1, x1):
        q = qb if self.colour == 0 else qw
        c = lw if q == qw else lb
        v = hw if q == qw else hb
        if (y == y1 and x != x1) or (x == x1 and y != y1): # Ladya movement
            return c.checker(y, x, y1, x1)
        elif (abs(y - y1) == 2 and abs(x - x1) == 1) or (
            abs(x - x1) == 2 and abs(y - y1) == 1 # Horse movement
        ):
            return v.checker(y, x, y1, x1)
        else:
            return False


class BHorse(ChessFigure):
    IMG = ("♗♘", "♝♞")

    def checker(self, y, x, y1, x1):
        q = qb if self.colour == 0 else qw
        c = cw if q == qw else cb
        v = hw if q == qw else hb
        if (x + y == x1 + y1) or (x + y1 == y + x1): # Bishop movement
            return c.checker(y, x, y1, x1)
        elif (abs(y - y1) == 2 and abs(x - x1) == 1) or (
            abs(x - x1) == 2 and abs(y - y1) == 1 # Horse movement
        ):
            return v.checker(y, x, y1, x1)
        else:
            return False


class QHorse(ChessFigure):
    IMG = ("♕♘", "♛♞")

    def checker(self, y, x, y1, x1):
        q = qb if self.colour == 0 else qw
        c = qw if q == qw else qb
        v = hw if q == qw else hb
        if x == x1 or y == y1 or (x + y == x1 + y1) or (x + y1 == y + x1): # king movement
            return c.checker(y, x, y1, x1)
        elif (abs(y - y1) == 2 and abs(x - x1) == 1) or (
            abs(x - x1) == 2 and abs(y - y1) == 1 # Horse movement
        ):
            return v.checker(y, x, y1, x1)
        else:
            return False

def input_cord(a): # input Coordinates
    while True:
        q = input(a)
        try:
            q = int(q)
        except:
            print("Data entered incorrectly")
        else:
            q = str(q)
            q = "0" + q if len(q) == 1 else q # If the number is a digit, put 0 before it
            if len(q) == 2 and 0 <= int(q) <= 77: # Enter the complete coordinates
                return q
            else:
                print("Data entered incorrectly")

dot = NoneType()
pb = Pawn(0) # 0 : black color
pw = Pawn(1) # 1: White color
kb = King(0, 0, 4) # 04: The position of the black king
kw = King(1, 7, 4) # 74: The position of the white king
qb = Quinn(0)
qw = Quinn(1)
lb = Ladya(0)
lw = Ladya(1)
hb = Horse(0)
hw = Horse(1)
cb = Bishop(0)
cw = Bishop(1)
qhw = QHorse(1)
qhb = QHorse(0)
lhb = LHorse(0)
lhw = LHorse(1)
chb = BHorse(0)
chw = BHorse(1)

class Board:
    def __init__(self):
        self.i = 1
        self.dot = dot
        self.pb = pb # 0 : black color
        self.pw = pw # 1: White color
        self.kb = kb # 04: The position of the black king
        self.kw = kw  # 74: The position of the white king
        self.qb = qb
        self.qw = qw
        self.lb = lb
        self.lw = lw
        self.hb = hb
        self.hw = hw
        self.cb = cb
        self.cw = cw
        self.qhw = qhw
        self.qhb = qhb
        self.lhb = lhb
        self.lhw = lhw
        self.chb = chb
        self.chw = chw
        self.board = [
            [lb, hb, cb, qb, kb, cb, hb, lb],
            [pb, pb, pb, pb, pb, pb, pb, pb],
            [dot, dot, dot, dot, dot, dot, dot, dot],
            [dot, dot, dot, dot, dot, dot, dot, dot],
            [dot, dot, dot, dot, dot, dot, dot, dot],
            [dot, dot, dot, dot, dot, dot, dot, dot],
            [pw, pw, pw, pw, pw, pw, pw, pw],
            [lw, hw, cw, qw, kw, cw, hw, lw],
        ]

        copy_board = copy.deepcopy(self.board) # deepcopy...
        self.reboard = [copy_board]

    def pboard(self):
        print("-" * 35) # Terminal output
        for i in t.board:
            for j in i:
                print(j, end="   ")
            print()
            print(j, end=" ")
        print("-" * 35)

    def checker(self, y, x, y1, x1):
        if (
            t.board[y1][x1].colour == -10 # Empty or checkered house
            or abs(t.board[y1][x1].colour - t.board[y][x].colour) == 1
        ):
            win_current = self.board[y][x].checker(y, x, y1, x1)
            return win_current
        else:
            return False

    def can_beat(self, y, x):
        win_current_can = False
        for v, i in enumerate(t.board): 
            for k, j in enumerate(i):
                if t.checker(v, k, y, x):
                    win_current_can = True
        return win_current_can

    def eszkere(self, y, x): # Scale
        for v, i in enumerate(t.board):
            for k, j in enumerate(i):
                if t.checker(v, k, y, x):
                    return (v, k)

    def echis(self, y, x): # writes the house index
        moves = []
        for v, i in enumerate(t.board):
            for k, j in enumerate(i):
                if t.checker(y, x, v, k) and not t.can_move(y, x, v, k):
                    moves.append((v, k))
        return moves

    def can_move(self, y, x, y1, x1): # Whether the house is empty or not, the piece moves, so the previous house becomes empty
        q = kw if t.board[y][x].colour == 1 else kb
        if t.board[y][x].__class__ != King:
            if t.can_beat(q.y, q.x):
                save = t.board[y1][x1]
                t.board[y1][x1] = dot
                win_current = t.can_beat(q.y, q.x)
                t.board[y1][x1] = save
            else:
                save = t.board[y][x]
                save1 = t.board[y1][x1]
                t.board[y1][x1] = t.board[y][x]
                t.board[y][x] = dot
                win_current = t.can_beat(q.y, q.x)
                t.board[y][x] = save
                t.board[y1][x1] = save1
            return win_current
        else:
            save = t.board[y1][x1]
            t.board[y1][x1] = q
            win_current = t.can_beat(y1, x1)
            t.board[y1][x1] = save
            return win_current

    def mat(self):
        win_current_mat1 = True
        win_current_mat2 = []
        for v, i in enumerate(t.board):
            for k, j in enumerate(i):
                if t.checker(v, k, kw.y, kw.x) or t.checker(v, k, kb.y, kb.x): #  king Coordinates
                    q = kw if t.board[v][k].colour == 0 else kb
                    if self.can_beat(v, k) and not self.can_move( # Matte simulation
                        self.eszkere(v, k)[0], self.eszkere(v, k)[1], v, k
                    ):
                        win_current_mat1 = True
                    else:
                        win_current_mat1 = False
                    for i in range(-1, 2): 
                        for j in range(-1, 2):
                            try:
                                if t.checker(q.y, q.x, q.y + i, q.x + j):
                                    save = t.board[q.y + i][q.x + j]
                                    ultra_save = t.board[q.y][q.x] # King's current coordinates
                                    t.board[q.y][q.x] = dot # The previous house should be empty
                                    t.board[q.y + i][q.x + j] = q
                                    if t.can_beat(q.y + i, q.x + j):
                                        t.board[q.y + i][q.x + j] = save
                                        t.board[q.y][q.x] = ultra_save
                                        win_current_mat2.append(False)
                                    else:
                                        t.board[q.y + i][q.x + j] = save
                                        t.board[q.y][q.x] = ultra_save
                                        win_current_mat2.append(True)
                                else:
                                    win_current_mat2.append(False)
                            except:
                                win_current_mat2.append(False)
                                continue
        if True in win_current_mat2:
            win_current_mat2 = True
        else:
            win_current_mat2 = False
        return win_current_mat1 + win_current_mat2

    def check_next(self, y, x):
        can_move = []
        moves = [(2, 2), (2, -2), (-2, 2), (-2, -2)]
        for i in range(0, 4):
            try:
                y1 = y + moves[i][0] # New coordinates 
                x1 = x + moves[i][1]
                if self.shcan_beat(y, x, y1, x1)[0]:
                    can_move.append((y + moves[i][0], x + moves[i][1]))
            except:
                continue
        return can_move

    def recoil_board(self, q):  # undo
        while True:
            try:
                q = int(q)
            except:
                t.recoil_board(q)
            else:
                if 0 < q <= len(t.reboard) - 1: # Simulation of return movement
                    a = t.reboard[-(q + 1)]
                    a = copy.deepcopy(a)
                    t.board = a
                    t.i -= q
                    t.reboard = t.reboard[: len(t.reboard) - q]
                    return a
                else:
                    t.recoil_board(q)

t = Board()
