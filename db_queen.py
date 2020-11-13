from sqlalchemy import (
    create_engine,
    Table,
    Column,
    String,
    Integer,
    MetaData,
    UniqueConstraint,
)
from config import postgres_local_base
from sqlalchemy import select, and_
from ast import literal_eval
# from n_queens import NQueens


class DbQueen:
    def __init__(self):
        self.meta = MetaData()

        self.engine = create_engine(postgres_local_base, echo=True)

        self.queen_solved = Table(
            "queen_solved",
            self.meta,
            Column("id", Integer, primary_key=True),
            Column("pieces", Integer),
            Column("solution", String),
            UniqueConstraint(
                "pieces",
                "solution",
                name="uniq_pieces_solution",
            ),
        )

        self.meta.create_all(self.engine)

    def db_save_solution(self, positions: list, size: int):
        """
        Save the solution on database.
        """
        try:
            conn = self.engine.connect()
            stmt = select([self.queen_solved]).where(
                and_(
                    self.queen_solved.c.pieces == size,
                    self.queen_solved.c.solution == f"{positions}",
                )
            )
            result = conn.execute(stmt)
            if result.rowcount == 0:
                ins = self.queen_solved.insert(None).values(
                    pieces=size,
                    solution=f"{positions}",
                )
                conn.execute(ins)
        except Exception as e:
            print(e)

    def db_get_solutions(
        self,
        size: int,
        short_board: bool,
        full_board: bool,
    ):
        """
        Get the solutions saved on database.
        """
        solutions = 0
        try:
            conn = self.engine.connect()
            stmt = select([self.queen_solved]).where(
                self.queen_solved.c.pieces == size,
            )
            result = conn.execute(stmt)
            print(result.rowcount)
            for row in result:
                solutions += 1
                positions = literal_eval(row[2])
                if full_board or short_board:
                    print(f"--Solution:{solutions}--")
                if short_board:
                    NQueens(size=size).show_short_board(positions)
                if full_board:
                    NQueens(size=size).show_full_board(positions)

        except Exception as e:
            print(e)
