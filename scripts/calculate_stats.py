import db_manager.db as db

def calculate_stats():
    db.reset_player_stats()

    players = db.get_pool_players()
    for player in players:
        data = (player,)
        games = db.get_games_by_player(data)

        total_games = len(games)

        total_wins = 0
        for is_win in games:
            if is_win == True:
                total_wins += 1
        
        win_percentage = (total_wins / total_games) * 100
        win_percentage = f"{win_percentage:.2f}%" 

        data = (player, total_games, total_wins, win_percentage)
        db.save_player_stats(data)

        print(player + ' total_games: ' + str(total_games) 
              + " , total_wins: " + str(total_wins) 
              + " , win% : " + str(win_percentage))


if __name__ == '__main__':
    print("STARTING calculate_stats()")
    calculate_stats()
    print("FINISHED calculate_stats()")