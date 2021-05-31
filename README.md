# Battery Stats
A module created for easily reading the current parameters of Battery in realtime.

---

## Installation
Clone this repository into the location you want to use, and directly use it as a module. (or download the zip, extract and directly use, as a module)

---

## Usage
```python
from batteryutils import Battery

print(Battery().all_stats)
```

outputs :

```shell
   Battery Information
-----------------------
Date         : 2021-05-31
Time         : 18:29:33
Capacity     : 94
Charge Now   : 2174000
Charge Full  : 2311000
```
