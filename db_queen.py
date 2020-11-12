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

meta = MetaData()

engine = create_engine(postgres_local_base, echo=True)

queen_solved = Table(
    "queen_solved",
    meta,
    Column("id", Integer, primary_key=True),
    Column("pieces", Integer),
    Column("solution", String),
    UniqueConstraint("pieces", "solution", name="unique_pieces_solution"),
)
