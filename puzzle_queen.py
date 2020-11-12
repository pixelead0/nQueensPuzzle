import click
from n_queens import NQueens
import time
from datetime import timedelta


@click.command()
@click.option(
    "-n",
    "--pieces",
    default=8,
    help="Number of queens (default=8).",
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
@click.option(
    "-db",
    "--save_db",
    is_flag=True,
    default=False,
    help="Save the solutions on database.",
)
@click.option(
    "-g",
    "--get_db",
    is_flag=True,
    default=False,
    help="Get the solutions from database (this option exclude -db).",
)
def calculate_solution(pieces, full_board, short_board, save_db, get_db):
    """The eight queens puzzle in Python."""
    t = time.process_time()

    queens = NQueens(pieces, full_board, short_board, save_db, get_db)
    solutions = queens.solve()
    print(f"Found {solutions} solutions.")

    elapsed_time = timedelta(seconds=time.process_time() - t)
    print(f"Time elapsed (hh:mm:ss.ms) {elapsed_time}")


if __name__ == "__main__":
    calculate_solution()  # pylint: disable=no-value-for-parameter
