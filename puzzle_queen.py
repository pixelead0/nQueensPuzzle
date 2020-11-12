import click
from n_queens import NQueens
import time
from datetime import timedelta


@click.command()
@click.option(
    "-n",
    "--pieces",
    default=8,
    help="Number of queens.",
)
@click.option(
    "-f",
    "--full_board",
    is_flag=True,
    default=False,
    help="Show solutions on full NxN board.",
)
@click.option(
    "-s",
    "--short_board",
    is_flag=True,
    default=False,
    help=""" Show the queens positions on the board in compressed form,
        each number represent the occupied column position in the
        corresponding row.
        """,
)
def calculate_solution_queens(pieces, full_board, short_board):
    """The eight queens puzzle in Python."""
    t = time.process_time()

    queens = NQueens(pieces, full_board, short_board)
    solutions = queens.solve()
    print(f"Found {solutions} solutions.")

    elapsed_time = timedelta(seconds=time.process_time() - t)
    print(f"Time elapsed (hh:mm:ss.ms) {elapsed_time}")


if __name__ == "__main__":
    calculate_solution_queens()  # pylint: disable=no-value-for-parameter
