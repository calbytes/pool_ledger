import db_manager.db as db
from datetime import datetime
from scripts.stats import calculate_stats

def get_match_input():
    print("___MATCH ENTRY___")

    week_num = ''
    while week_num == '':
        week_num_input = input("Enter week number: ").strip()
        if week_num_input.isdigit():
            week_num = int(week_num_input)
        else:
            print("--->>>Invalid entry. Re-Enter week number.<<<")

    opponent = ''
    while opponent == '':
        opponent_input = input("Enter opponent team's name: ").strip()
        if opponent_input is None or opponent_input=='':
            print("--->>>Re-Enter opponent's team name.<<<")
        else:
            opponent = opponent_input

    is_win = ''
    while is_win == '':
        win_input = input("Enter [W]in or [L]oss : ").lower()
        if win_input=='w' or win_input=='l':
            if win_input == 'w':
                is_win = bool(True)
            else:
                is_win = bool(False)
        else:
            print("--->>>Invalid win input. Enter W or L.<<<")

    match_score = ''
    while match_score == '':
        match_input = input("Enter match score in <int>:<int> format: ")
        scores = match_input.split(':')
        if len(scores)==2 and scores[0].isdigit() and scores[1].isdigit():
            match_score = match_input
        else:
            print("--->>>Invalid score input. Try again.<<<")

    match_date = ''
    while match_date == '':
        date_input = input("Enter match date in mm/dd/yy format: ")
        try:
            match_date = datetime.strptime(date_input, '%m/%d/%y')
        except:
            print("--->>>Invalid date input. Re-Enter in mm/dd/yy format<<<")

    return (week_num, opponent, is_win, match_score, match_date)


def get_game_results():
    print("\n___ROUND 1___")
    round1 = []
    while round1 == []:
        double_game_entry(1, round1)
        for game in range(2,6):
            single_game_entry(game, round1)

        print("\n___Verify Round 1___")
        for game in round1:
            print(game)
        is_correct = input("Valid? yes or no: ")
        if is_correct.lower() == 'yes':
            pass
        else:
            round1 = []

    print("\n___ROUND 2___")
    round2 = []
    while round2 == []:
        double_game_entry(6, round2)
        for game in range(7,11):
            single_game_entry(game, round2)
        double_game_entry(11, round2)

        print("\n___Verify Round 2___")
        for game in round2:
            print(game)
        is_correct = input("Valid? yes or no: ")
        if is_correct.lower() == 'yes':
            pass
        else:
            round2 = []

    return round1 + round2


def double_game_entry(game_id, round):
    input_parts = ""
    while input_parts == "":
        game_input = input(f"Enter Game {game_id} Doubles result: ")
        input_parts = game_input.split(" ")
        if len(input_parts)==3 and (input_parts[2].lower()=='w' or input_parts[2].lower()=='l'):
            player1 = input_parts[0].title()
            player2 = input_parts[1].title()
            is_win_input = input_parts[2].lower()
            if is_win_input == 'w':
                is_win = bool(True)
            else:
                is_win = bool(False)

            double1 = (game_id, "double", player1, is_win)
            double2 = (game_id, "double", player2, is_win)
            round.append(double1)
            round.append(double2)
        else:
            print("--->>>Re-Enter Doubles result in format: player1 player2 [W/L]<<<")
            input_parts = ""
            

def single_game_entry(game_id, round):
    input_parts = ""
    while input_parts == "":
        game_input = input(f"Enter Game {game_id} Singles result: ")
        input_parts = game_input.split(" ")
        if len(input_parts)==2 and (input_parts[1].lower()=='w' or input_parts[1].lower()=='l'):
            player = input_parts[0].title()
            is_win_input = input_parts[1].lower()
            if is_win_input == 'w':
                is_win = bool(True)
            else:
                is_win = bool(False)
            
            game = (game_id, "single", player, is_win)
            round.append(game)
        else:
            print("--->>>Re-Enter Singles result in format: player1 [W/L] <<<")
            input_parts = ""


def enter_score_sheet():
    match_input = get_match_input()
    db.insert_match_entry(match_input)

    match_id = match_input[0]
    match_date = match_input[4]
    game_results = get_game_results()
    for game in game_results:
        data = (match_id,) + game + (match_date,)
        db.insert_game_entry(data)
    print("\nGame entries saved!")


if __name__ == '__main__':
    print("STARTING match_entry")
    enter_score_sheet()
    print("FINISHED match_entry")
    calculate_stats()