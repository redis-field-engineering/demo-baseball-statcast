from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher

playerid_lookup('cueto', 'johnny')
cueto_stats = statcast_pitcher('2021-06-01', '2021-06-30', 456501)
cueto_stats.to_csv('cueto_june.csv')

