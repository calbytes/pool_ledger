class PSQL_QUERIES:

    INSERT_GAME_ENTRY = '''
        INSERT INTO pool_games
        (match_id, game_id, game_type, player, is_win, date)
        VALUES
        (%s, %s, %s, %s, %s, %s)
    '''

    INSERT_MATCH = '''
        INSERT INTO pool_match
        (match_id, opponent, is_win, match_score, date)
        VALUES
        (%s, %s, %s, %s, %s)
    '''

    SELECT_DISTINCT_POOL_PLAYERS = '''
        SELECT DISTINCT player
        FROM pool_games
        ORDER by (player);
    '''

    DELETE_POOL_PLAYER_STATS = '''
        DELETE
        FROM pool_player_stats
    '''

    SELECT_GAMES_BY_PLAYER = '''
        SELECT is_win
        FROM pool_games
        WHERE player = %s;
    '''

    INSERT_PLAYER_STATS = '''
        INSERT INTO pool_player_stats
        (player, total_games, total_wins, win_percentage)
        VALUES
        (%s, %s, %s, %s);
    '''