redis-cli RG.PYEXECUTE "$(cat historical_pitches.py)"
redis-cli RG.PYEXECUTE "$(cat real_time_pitches.py)"
