import psycopg
from .config import DB_CONFIG
from db_manager.psql_queries import PSQL_QUERIES as psql
from enum import Enum, auto

config = DB_CONFIG

class Fetch(Enum):
    ONE = auto()
    ALL = auto()
    EXC = auto()

def execute(psql_raw, fetch: Fetch, params=None):
    try:
        with psycopg.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(psql_raw, params)

                if fetch == Fetch.ONE:
                    row = cur.fetchone()
                    return row
                elif fetch == Fetch.ALL:
                    rows = cur.fetchall()
                    return rows
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise

def insert_match_entry(data):
    execute(psql.INSERT_MATCH, Fetch.EXC, data)

def insert_game_entry(data):
    execute(psql.INSERT_GAME_ENTRY, Fetch.EXC, data)


def todo(data):
    row = execute(psql.TODO, Fetch.ONE, data)
    return row

def todo1():
    rows = execute(psql.TODO, Fetch.ALL)