class PSQL_QUERIES:

    INSERT_GAME_ENTRY = '''
        INSERT INTO pool_games
        (match_id, game_id, game_type, player, is_win, date)
        VALUES
        (%s, %s, %s, %s, %s)
    '''

    INSERT_MATCH = '''
        INSERT INTO pool_match
        (match_id, opponent, is_win, match_score, date)
        VALUES
        (%s, %s, %s, %s, %s)
    '''