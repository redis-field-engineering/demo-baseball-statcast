def processPitch(pitch):
    """
    Add the pitch type to a sorted set
    """


    # Add the pitch count to a sorted set
    execute(
	    "ZINCRBY",
	    '{}:real_time_pitch_count'.format(pitch['value']['pitcher.1']),
	    1,
	    pitch['value']['pitch_name'])

    execute(
	    "HSET",
	    "current_pitch",
	    "pitch",
	    pitch['value']['pitch_name'],
	    "velocity",
	    pitch['value']['effective_speed'])

    execute("SET", "DEBUG", pitch)
    execute("HINCRBY", "current_game", "total_pitches", 1)
    execute("HINCRBY", "current_game", pitch['value']['description'], 1)
    execute('TS.INCRBY', "ts:count:%s" %(pitch['value']['pitch_name'].replace(" ", '')), 1, 'TIMESTAMP', int(pitch['id'].split('-')[0]))
    execute('TS.ADD', "ts:velocity:%s" %(pitch['value']['pitch_name'].replace(" ", '')), int(pitch['id'].split('-')[0]), pitch['value']['effective_speed'])


gb = GearsBuilder(
        reader = 'StreamReader',
        desc   = "Collect the real time pitch data")

gb.map(processPitch)
gb.register('RealTimePitches')
