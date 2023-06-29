from unittest import TestCase, main
from logic import *

class ComponentTestChess(TestCase):
    def test_undo(test_case):
        first = t.reboard # first state
        t.board[6][0], t.board[5][0] = dot, t.board[6][0]
        copy_board1 = copy.deepcopy(t.board)
        t.reboard.append(copy_board1) #move an element
        second = t.reboard # second state
        t.recoil_board(1) # call undo function
        third = t.reboard # third state
        assert second != third

def test_mat(test_case):
        res = t.mat()
        # game continues until a True or False response
        assert type(res) != bool

main()