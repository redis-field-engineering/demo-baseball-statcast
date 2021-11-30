def processPitch(pitch):
    """
    Add the pitch type to a sorted set
    """


    execute(
	    "ZINCRBY",
	    '{}:historical_pitch_count'.format(pitch['value']['pitcher.1']),
	    1,
	    pitch['value']['pitch_name'])

    current_set = execute("ZRANGE", '{}:historical_pitch_count'.format(pitch['value']['pitcher.1']), 0, -1, 'WITHSCORES')

    # recacluate the percentage for each pitch type
    current_count = current_set[1::2]
    current_pitch = current_set[::2]
    total_pitches = sum([int(i) for i in current_count])
    for i in range(len(current_count)):
	    execute(
		    "ZADD",
		    '{}:historical_pitch_percent'.format(pitch['value']['pitcher.1']),
		    round(100*int(current_count[i])/total_pitches,2),
		    current_pitch[i])
    execute("SET", "DEBUG", current_count)


gb = GearsBuilder(
        reader = 'StreamReader',
        desc   = "Collect the historical pitch data")

gb.map(processPitch)
gb.register('HistoricalPitches')
