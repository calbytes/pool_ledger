import db_manager.db as db

def get_all_pairs():
    pairs = set()

    match_ids = db.get_all_match_ids()
    for match_id in match_ids:
        data = (match_id)
        doubles = db.get_doubles_pairs_by_match_id(data)
        


    players = get_player_set(pairs)


def get_player_set(pairs):
    players = set()
    for pair in pairs:
        for player in pair:
            players.add(player)
    return players



if __name__ == '__main__':
    print("STARTING doubles_combo()\n")
    print("\nFINISHED doubles_combo()")
