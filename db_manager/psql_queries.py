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
        SELECT game_type, is_win
        FROM pool_games
        WHERE player = %s;
    '''

    INSERT_PLAYER_STATS = '''
        INSERT INTO pool_player_stats
        (player, total_games, total_wins, win_percentage, single_win_percentage, double_win_percentage)
        VALUES
        (%s, %s, %s, %s, %s, %s);
    '''

    INSERT_FILE = '''
        INSERT into pool_files
        (file_id, file_name, file_data)
        VALUES
        (%s, %s, %s)
    '''

    SELECT_FILE = '''
        SELECT file_data 
        FROM pool_files
        WHERE file_name = %s;
    '''

    GET_ALL_MATCH_IDS = '''
        SELECT match_id
        FROM pool_match
        ORDER BY match_id
    '''

    SELECT_DOUBLES_BY_MATCH_ID = '''
        SELECT player
        FROM pool_games
        WHERE match_id = %s
        AND game_id = %s
        AND game_type = 'double';
    '''

    GET_GAMES_BY_PLAYER_AND_MATCH_ID = '''
        SELECT game_type
        FROM pool_games
        WHERE player = %s
        and match_id = %s
    '''