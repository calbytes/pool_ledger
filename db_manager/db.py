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

def get_pool_players():
    rows = execute(psql.SELECT_DISTINCT_POOL_PLAYERS, Fetch.ALL)
    players = [row[0] for row in rows]
    return players

def reset_player_stats():
    execute(psql.DELETE_POOL_PLAYER_STATS, Fetch.EXC)

def get_games_by_player(data):
    rows = execute(psql.SELECT_GAMES_BY_PLAYER, Fetch.ALL, data)
    games = [row[0] for row in rows]
    return games

def save_player_stats(data):
    execute(psql.INSERT_PLAYER_STATS, Fetch.EXC, data)

def insert_file(data):
    execute(psql.INSERT_FILE, Fetch.EXC, data)

def select_file(data):
    file_data = execute(psql.SELECT_FILE, Fetch.ONE, data)
    return file_data[0]

