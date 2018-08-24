WeatherData
----------------------------
Weather data for Lahore from 1996 to 2011. Generate reports on the given data.


1. Annual Max/Min Temp: Formatted output as follows:
------------------------------------------------------------------------------
```sh
Year        MAX Temp        MIN Temp        MAX Humidity        MIN Humidity
------------------------------------------------------------------------------
1996        40                2               94                   20
1997        40                1               86                   10
1998        40                3               80                   30
```

2. Hottest days of each year
---------------------------------------------------
```sh
Year        Date          Temp
--------------------------------
2006        21/6/2006     45
2007        21/6/2007     47
2008        21/6/2008     46
2009        21/6/2009     43
```

This program  take two parameters e.g report number and weather data directory. According to above reports a usage output will be like:
```sh
Usage: weatherman [report#] [data_dir]

[Report #]
1 for Annual Max/Min Temperature
2 for Hottest day of each year

[data_dir]
Directory containing weather data files
```
Requirements
------------
- Python 3.6.3

Run the program. Thats it!
