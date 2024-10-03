import db_manager.db as db
from datetime import datetime

def get_match_input():
    print("___MATCH DETAILS___")
    try:
        print("Enter week number: ")
        week_num = int(input())

        print("Enter opponent team's name: ")
        opponent = str(input())

        print("Enter 1 for WIN, 0 for LOSS: ")
        is_win = bool(input())

        print("Enter match score in <num>:<num> format: ")
        match_score = str(input())

        print("Enter match date in mm/dd/yy format: ")
        date_input = str(input())
        match_date = datetime.strptime(date_input, '%m/%d/%y')

        return (week_num, opponent, is_win, match_score, match_date)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")

def enter_game_entries():
    print("___ROUND 1___")
    double_game_entry()
    for game in range(4):
        single_game_entry()

    print("___ROUND 2___")
    double_game_entry()
    for game in range(4):
        single_game_entry()
    double_game_entry()


def double_game_entry():
    try:
        add_game_entry(1)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
    print("in double")

def single_game_entry():
    try:
        add_game_entry(1)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
    print("in double")

def add_game_entry(game_input):
    pass

def enter_score_sheet():
    match_input = get_match_input()
    print(match_input)

    match_id = match_input[0]
    match_date = match_input[4]
    print(match_id)
    print(match_date)

    db.insert_match_entry(match_input)

    enter_game_entries()



if __name__ == '__main__':
    print("STARTING match_entry")
    enter_score_sheet()
    print("FINISHED match_entry")