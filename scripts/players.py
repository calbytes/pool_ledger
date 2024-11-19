import db_manager.db as db

def get_all_players():
    players = db.get_pool_players()

    #Remove retired players and forfeit players
    players.remove("forfeit")
    players.remove("Jacob")

    return players

