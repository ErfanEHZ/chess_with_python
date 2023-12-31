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

    def test_kish(test_case):
        result = t.can_beat(7, 4) #coordinates of king
        assert result == False


class UnitTestChess(TestCase): # testing true movements of each element.
    def test_layda(test_case):
        ladya = Ladya(0)
        result = ladya.checker(0, 0, 1, 0)
        assert result == True

    def test_horse(test_case):
        horse = Horse(0)
        result = horse.checker(0, 1, 2, 0)
        assert result == True

    def test_bishop(test_case):
        bishop = Bishop(0)
        result = bishop.checker(0, 2, 2, 0)
        assert result == False

    def test_quinn(test_case):
        quinn = Quinn(0)
        result = quinn.checker(0, 3, 4, 7)
        assert result == False

    def test_king(test_case):
        king = King(0, 0, 4)
        result = king.checker(0, 4, 1, 4)
        assert result == True

    def test_pawn(test_case):
        pawn = Pawn(0)
        result = pawn.checker(1, 2, 2, 2)
        assert result == True

main()
