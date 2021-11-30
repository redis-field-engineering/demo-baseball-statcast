def processPitch(pitch):
    """
    Add the pitch type to a sorted set
    """


    # Add the pitch count to a sorted set
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

    # Average the pitch speed per pitch type
    count_by_pitch = execute(
	    "HINCRBY",
	    '{}:historical_pitch_speed:{}'.format(pitch['value']['pitcher.1'], pitch['value']['pitch_type']),
	    'count',
	    1 )
    if int(count_by_pitch) == 1:
	    new_avg = pitch['value']['effective_speed']
    else:
	    avg_by_pitch = execute(
		    "HGET",
		    '{}:historical_pitch_speed:{}'.format(pitch['value']['pitcher.1'], pitch['value']['pitch_type']),
		    'average')
	    new_average = ((count_by_pitch - 1) * float(avg_by_pitch) + float(pitch['value']['effective_speed']))/int(count_by_pitch)

    execute(
	"HSET",
    	'{}:historical_pitch_speed:{}'.format(pitch['value']['pitcher.1'], pitch['value']['pitch_type']),
    	'average',
	pitch['value']['effective_speed'])



gb = GearsBuilder(
        reader = 'StreamReader',
        desc   = "Collect the historical pitch data")

gb.map(processPitch)
gb.register('HistoricalPitches')
