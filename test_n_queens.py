from n_queens import NQueens

pieces = 8
full_board = False
short_board = False
save_db = False
get_db = False


def test_one_queen():
    pieces = 1
    queens = NQueens(pieces)
    solutions = queens.solve()
    assert solutions == 1


def test_two_queens():
    pieces = 2
    queens = NQueens(pieces)
    solutions = queens.solve()
    assert solutions == 0


def test_three_queens():
    pieces = 3
    queens = NQueens(pieces)
    solutions = queens.solve()
    assert solutions == 0


def test_four_queens():
    pieces = 4
    queens = NQueens(pieces)
    solutions = queens.solve()
    assert solutions == 2


def test_five_queens():
    pieces = 5
    queens = NQueens(pieces)
    solutions = queens.solve()
    assert solutions == 10


def test_six_queens():
    pieces = 6
    queens = NQueens(pieces)
    solutions = queens.solve()
    assert solutions == 4


def test_seven_queens():
    pieces = 7
    queens = NQueens(pieces)
    solutions = queens.solve()
    assert solutions == 40


def test_eigth_queens():
    pieces = 8
    queens = NQueens(pieces)
    solutions = queens.solve()
    assert solutions == 92


def test_nine_queens():
    pieces = 9
    queens = NQueens(pieces)
    solutions = queens.solve()
    assert solutions == 352


def test_ten_queens():
    pieces = 10
    queens = NQueens(pieces)
    solutions = queens.solve()
    assert solutions == 724


def test_eleven_queens():
    pieces = 11
    queens = NQueens(pieces)
    solutions = queens.solve()
    assert solutions == 2680


def test_twelve_queens():
    pieces = 12
    queens = NQueens(pieces)
    solutions = queens.solve()
    assert solutions == 14200
