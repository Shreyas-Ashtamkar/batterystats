# Battery Stats
![Image](icon.png)

A [python3](https://www.python.org/) module created for easily reading the current parameters of Battery in realtime. It reads battery stats from `/sys/class/power_supply/` and returns. This module can be applied in a [verity of projects](#where-can-we-use-this). 

## Installation
Clone this repository into the location you want to use, and directly use it as a module. (or [download the zip](https://github.com/Shreyas-Ashtamkar/battery-stats/archive/refs/heads/main.zip), extract and directly use, as a module.)

## Usage

##### code
```python
from batteryutils import Battery

print(Battery().all_stats)
```

##### outputs :

```shell
   Battery Information
-----------------------
Date         : 2021-05-31
Time         : 18:29:33
Capacity     : 94
Charge Now   : 2174000
Charge Full  : 2311000
```

## Where can we use this?
+ Get battery stats on command line
+ Scripts ( Alert/Report generation )
+ Other Python Applicaitons
