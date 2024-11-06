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

    return doubles_map

def get_doubles_combinations(doubles_map):
    players = db.get_pool_players()
    players.remove('Jacob')

    double_combinations = {}
    for player in players:
        double_combinations[player] = [other_player for other_player in players if other_player != player]
    
    return double_combinations

def get_missing_double_pairs(doubles, combos):
    for player in doubles:
        if player not in combos:
            continue

        partners = doubles[player]

        for partner in partners:
            if partner in combos[player]:
                combos[player].remove(partner)
    
    return combos

if __name__ == '__main__':
    print("STARTING doubles_combo()\n")
    
    doubles_map = build_doubles_map()

    print("Doubles Played:")
    for player in doubles_map:
        print(player + " - " + str(doubles_map[player]))
        
    combo_map = get_doubles_combinations(doubles_map)

    print("\nMissing double pairs: ")
    missing_pairs_map = get_missing_double_pairs(doubles_map, combo_map)
    for player in missing_pairs_map:
        print(player + " - " + str(missing_pairs_map[player]))

    print("\nFINISHED doubles_combo()")
