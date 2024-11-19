import db_manager.db as db
import scripts.players as team_members

players = team_members.get_all_players()

def update_stats():
    reset_previous_stats()
    calculate_stats()

def reset_previous_stats():
    print("Resetting previous stats...\n")
    db.reset_player_stats()

def calculate_stats():
    for player in players:
        data = (player,)
        games = db.get_games_by_player(data)

        total_games = len(games)
        total_wins = 0
        total_single_games = 0
        total_single_wins = 0
        total_double_games = 0
        total_double_wins = 0

        for game in games:
            game_type = game[0]
            is_win = game[1]

            if is_win:
                total_wins += 1

            if game_type == "single":
                total_single_games += 1
                if is_win:
                    total_single_wins += 1

            elif game_type == "double":
                total_double_games += 1
                if is_win:
                    total_double_wins += 1
        
        total_win_percentage = (total_wins / total_games) * 100
        total_win_percentage = f"{total_win_percentage:.2f}%" 

        single_win_percentage = (total_single_wins / total_single_games) * 100
        single_win_percentage = f"{single_win_percentage:.2f}%"  

        double_win_percentage = (total_double_wins / total_double_games) * 100
        double_win_percentage = f"{double_win_percentage:.2f}%"

        print("\nPlayer: " + player)
        print("Total Games: " + str(total_games))
        print("Total Win Percentage: " + total_win_percentage)
        print("Total Single Win Perentage: " + single_win_percentage)
        print("Total Doubles Win Percentage: " + double_win_percentage)

        data = (player, total_games, total_wins, total_win_percentage, single_win_percentage, double_win_percentage)
        db.save_player_stats(data) 


if __name__ == '__main__':
    print("STARTING update_stats()\n")
    update_stats()
    print("FINISHED update_stats()")