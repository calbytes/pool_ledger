import db_manager.db as db
from datetime import datetime

def get_match_input():
    print("___MATCH ENTRY___")
    print("Enter week number: ")
    week_num = ''
    while week_num == '':
        week_num_input = input().strip()
        if week_num_input.isdigit():
            week_num = int(week_num_input)
        else:
            print("--->>>Invalid entry. Re-Enter week number.<<<")

    print("Enter opponent team's name: ")
    opponent = ''
    while opponent == '':
        opponent_input = input().strip()
        if opponent_input is None or opponent_input=='':
            print("--->>>Re-Enter opponent's team name.<<<")
        else:
            opponent = opponent_input

    print("Enter 1 for WIN, 0 for LOSS: ")
    is_win = ''
    while is_win == '':
        win_input = input()
        if win_input.isdigit() and (win_input=='0' or win_input=='1'):
            is_win = bool(win_input)
        else:
            print("--->>>Invalid win input. Enter 0 or 1.<<<")

    print("Enter match score in <int>:<int> format: ")
    match_score = ''
    while match_score == '':
        match_input = str(input())
        scores = match_input.split(':')
        if len(scores)==2 and scores[0].isdigit() and scores[1].isdigit():
            match_score = match_input
        else:
            print("--->>>Invalid score input. Try again.<<<")

    print("Enter match date in mm/dd/yy format: ")
    match_date = ''
    while match_date == '':
        date_input = str(input())
        try:
            match_date = datetime.strptime(date_input, '%m/%d/%y')
        except:
            print("--->>>Invalid date input. Re-Enter in mm/dd/yy format<<<")

    return (week_num, opponent, is_win, match_score, match_date)


def get_game_results():
    print("___ROUND 1___")
    round1 = []
    while round1 == []:
        round1.append(get_double_game_entry(1))
        for game in range(2,6):
            round1.append(get_single_game_entry(game))
        print("\n___Verify Round 1___")
        print(round1)
        print("Enter yes or no")
        is_correct = input()
        if is_correct == 'yes':
            pass
        else:
            round1 = []

    print("___ROUND 2___")
    round2 = []
    while round2 == []:
        round2.append(get_double_game_entry(6))
        for game in range(7,11):
            round2.append(get_single_game_entry(game))
        round2.append(get_double_game_entry(11))
        print("\n___Verify Round 2___")
        print(round1)
        print("Enter yes or no")
        is_correct = input()
        if is_correct == 'yes':
            pass
        else:
            round2 = []

    return round1 + round2


def get_double_game_entry(game_id):
    game = []
    print(f"Enter Game {game_id} Doubles result in format: player1 player2 [w/l]")
    while game == []:
        game_input = input()
        input_parts = game_input.split(" ")
        if len(input_parts)==3 and (input_parts[2].lower()=='w' or input_parts[2].lower()=='l'):
            player1 = input_parts[0]
            player2 = input_parts[1]
            is_win = input_parts[2].lower()

            double1 = (game_id, "double", player1, is_win)
            double2 = (game_id, "double", player2, is_win)
            game.append(double1)
            game.append(double2)
        else:
            print("--->>>Re-Enter Doubles result.<<<")

    return game
            

def get_single_game_entry(game_id):
    game = []
    print(f"Enter Game {game_id} Singles result in format: player1 player2 [w/l]")
    while game == []:
        game_input = input()
        input_parts = game_input.split(" ")
        if len(input_parts)==2 and (input_parts[1].lower()=='w' or input_parts[1].lower()=='l'):
            player = input_parts[0]
            is_win = input_parts[1].lower()

            double1 = (game_id, "single", player, is_win)
            game.append(double1)
        else:
            print("--->>>Re-Enter Singles result.<<<")

    return game


def add_game_entry(data):
    print(data)

def enter_score_sheet():
    match_input = get_match_input()
    db.insert_match_entry(match_input)

    match_id = match_input[0]
    match_date = match_input[4]
    game_results = get_game_results()
    for game in game_results:
        data = (match_id,) + game + (match_date,)
        add_game_entry(data)



if __name__ == '__main__':
    print("STARTING match_entry")
    enter_score_sheet()
    print("FINISHED match_entry")