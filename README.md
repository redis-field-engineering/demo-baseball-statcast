## Example of processing statcast data in real time using Redis Gears and time series.


### Grab some data

```
>>> from pybaseball import statcast_pitcher
>>> from pybaseball import playerid_lookup
>>> playerid_lookup('cueto', 'johnny')
>>> ytd=statcast_pitcher('2021-04-01', '2021-08-02', 456501)
>>> today=statcast_pitcher('2021-08-03', '2021-08-03', 456501)
>>> today.to_csv('cueto_0803.csv')
>>> ytd.to_csv('cueto_ytd.csv')
```


### Load the historical data

```
redis-cli flushdb && ./load_gears.sh && ./stream_data.py cueto_ytd.csv HistoricalPitches
```

### Run the real-time data

```
./stream_data.py cueto_0803.csv RealTimePitches 1500
```
