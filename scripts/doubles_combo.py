import db_manager.db as db

def get_all_doubles():
    doubles = []
    match_ids = db.get_all_match_ids()
    for match_id in match_ids:
        for game in [1,6,11]:
            data = (match_id, game)
            doubles_players = db.get_double_players(data)
            doubles.append(doubles_players)
    return doubles

def build_doubles_map():
    doubles_map = {}
    doubles = get_all_doubles()

    for double in doubles:
        player1 = double[0]
        if player1 not in doubles_map:
            doubles_map[player1] = []

        player2 = double[1]
        if player2 not in doubles_map:
            doubles_map[player2] = []

        doubles_map[player1].append(player2)
        doubles_map[player2].append(player1)

    for player in doubles_map:
        print(player + " - " + str(len(doubles_map[player])))
        #print(str(doubles_map[player]))

    return doubles_map


if __name__ == '__main__':
    print("STARTING doubles_combo()\n")
    doubles_map = build_doubles_map()
    print("\nFINISHED doubles_combo()")
