import db_manager.db as db

def get_all_players():
    players = db.get_pool_players()

    #Remove retired players and forfeit players
    players.remove("forfeit")
    players.remove("Jacob")

    return players

def player_metadata():
    players = get_all_players()
    match_ids = db.get_all_match_ids()
    total_matches = len(match_ids)

    for player in players:
        attendance = 0
        total_games = 0
        total_single_games = 0
        total_double_games = 0

        for match in match_ids:
            data = (player, match,)
            games = db.get_games_by_player_and_match_id(data)
            games_per_match = len(games)

            if games_per_match != 0:
                attendance += 1
            
            for game_type in games:
                total_games += 1
                if game_type == "single":
                    total_single_games += 1
                elif game_type == "double":
                    total_double_games += 1

        average_games_per_match = total_games / attendance
        average_games_per_match = f"{average_games_per_match:.2f}"
        
        print("Player: " + player)
        print(f"Attended {attendance} out of {total_matches} matches")
        print(f"Average games per match: {average_games_per_match}")
        print(f"Total Single Games Played: {total_single_games}")
        print(f"Total Double Games Played: {total_double_games}\n")

if __name__ == '__main__':
    print("\nPlayer MetaData()\n")
    player_metadata()
