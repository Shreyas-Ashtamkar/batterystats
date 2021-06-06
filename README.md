![Image](icon.png)

# Battery Stats
![Build Status](https://github.com/Shreyas-Ashtamkar/battery-stats/actions/workflows/mytests.yml/badge.svg)

A [python3](https://www.python.org/) module created for easily reading the current parameters of Battery in realtime. It reads battery stats from `/sys/class/power_supply/` and returns. This module can be applied in a [verity of projects](#where-can-we-use-this). 

## Installation
Clone this repository into the same folder you want to write code in, and directly use it as a module. (or [download the zip](https://github.com/Shreyas-Ashtamkar/battery-stats/archive/refs/heads/main.zip), extract and directly use, as a module.)

## Usage

##### code ( python3 )
```python
from batterystats import Battery

print(Battery())
```

##### outputs :

```shell
          Battery Information           
----------------------------------------
Date - Time  : 2021-06-01 | 12:44:06
Battery Path : /sys/class/power_supply/BAT0
Status       : Discharging
Capacity     : 63%
Charge Now   : 1469000
Charge Full  : 2311000
```

## Where can we use this?
+ Get battery stats on command line
+ Scripts ( Alert/Report generation )
+ Other Python Applicaitons
 
