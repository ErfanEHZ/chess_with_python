from logic import *

if __name__ == '__main__':
    i = 1
    clr = ("black", "white")
    print("Start the Game ?")
    game = input("1) Yes\n2 )No\n")
    if game == "1":
        while t.mat():
            vvod = input("Enter what you want to do (Move : 1, Undo : 2, View moves : 3): ")
            t.pboard()
            if vvod == "1":
                print(f" walking.. {clr[i % 2]}")
                cord1 = input_cord(
                    "Enter the coordinates of the figure you want to resemble: "
                )
                cord2 = input_cord("Enter where you want to go: ")
                y = int(cord1[0])
                x = int(cord1[1])
                y1 = int(cord2[0])
                x1 = int(cord2[1])
                if t.board[y][x].colour == i % 2:
                    if t.checker(y, x, y1, x1) and not t.can_move(y, x, y1, x1):
                        if t.board[y][x].__class__ == King:
                            t.board[y][x].y = y1
                            t.board[y][x].x = x1
                        t.board[y][x], t.board[y1][x1] = dot, t.board[y][x]
                        copy_board1 = copy.deepcopy(t.board)
                        t.reboard.append(copy_board1)
                        t.pboard()
                        print("\n" * 3)
                        if t.can_beat(kw.y, kw.x):
                            print("Check to the white king")
                        elif t.can_beat(kb.y, kb.x):
                            print("Check to the black king")
                    else:
                        print()
                        print("Wrong move, try something else")
                        continue
                else:
                    print("\n" * 3)
                    print("Wrong move, try something else")
                    continue
                i += 1
            elif vvod == "2":
                q = input(f"Enter how many moves you want to roll back the game (max: : {len(t.reboard) - 1}): ")# reboard =  dep copy
                t.recoil_board(q)
                t.pboard()
            elif vvod == "3":
                codr1, cord2 = input_cord(
                    "Enter the moves of which piece you want to see: "
                )
                codr1 = int(codr1)
                cord2 = int(cord2)
                for i, v in t.echis(codr1, cord2):
                    if t.board[i][v].__class__ != NoneType:
                        t.board[i][v] = f"({t.board[i][v]})"
                    else:
                        t.board[i][v] = "■"
                t.pboard()
                a = copy.deepcopy(t.reboard[-1])
                t.board = a
            else:
                continue
        else:
            print(f"Game over, win {clr[(i - 1) % 2]}")
            t.pboard()

