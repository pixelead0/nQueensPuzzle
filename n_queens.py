"""
This program it's based on N-Queens-Puzzle implemented
by Paul Silisteanu (@sol-prog).
    https://github.com/sol-prog/N-Queens-Puzzle
"""

from sqlalchemy import select, and_
from db_queen import queen_solved, engine, meta


class NQueens:
    """Generate all valid solutions for the n queens puzzle."""

    def __init__(self, size: int, full_board: bool, short_board: bool):
        # Store the puzzle (problem) size and the number of valid solutions
        meta.create_all(engine)
        self.size = size
        self.full_board = full_board
        self.short_board = short_board
        self.solutions = 0

    def solve(self) -> int:
        """Solve the n queens puzzle and print the number of solutions."""
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        return self.solutions

    def put_queen(self, positions: list, target_row: int):
        """
        Try to place a queen on target_row by checking all N possible cases.
        If a valid place is found the function calls itself trying to
        place a queen on the next row until all N queens are placed on the
        NxN board.
        """
        # Base (stop) case - all N rows are occupied
        if target_row == self.size:
            self.solutions += 1
            if self.full_board or self.short_board:
                print(f"--Solution:{self.solutions}--")
            if self.short_board:
                self.show_short_board(positions)
            if self.full_board:
                self.show_full_board(positions)
            try:
                conn = engine.connect()
                stmt = select([queen_solved]).where(
                    and_(
                        queen_solved.c.pieces == self.size,
                        queen_solved.c.solution == f"{positions}",
                    )
                )
                result = conn.execute(stmt)
                if result.rowcount == 0:
                    ins = queen_solved.insert(None).values(
                        pieces=self.size,
                        solution=f"{positions}",
                    )
                    conn.execute(ins)
            except Exception as e:
                print(e)

        else:
            # For all N columns positions try to place a queen
            for column in range(self.size):
                # Reject all invalid positions
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)

    def check_place(
        self,
        positions: list,
        ocuppied_rows: int,
        column: int,
    ) -> bool:
        """
        Check if a given position is under attack from any of
        the previously placed queens (check column and diagonal positions)
        """
        # print(positions)
        for i in range(ocuppied_rows):
            if (
                positions[i] == column
                or positions[i] - i == column - ocuppied_rows
                or positions[i] + i == column + ocuppied_rows
            ):
                # print(positions[i], column)
                return False
        return True

    def show_full_board(self, positions: list):
        """Show the full NxN board"""
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

    def show_short_board(self, positions: list):
        """
        Show the queens positions on the board in compressed form,
        each number represent the occupied column position in the
        corresponding row.
        """
        line = ""
        for i in range(self.size):
            line += str(positions[i]) + " "
        print(line)
