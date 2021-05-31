from os import listdir as ls
from os.path import isfile
from datetime import datetime

class _Battery:
    def __init__(self, no=0) -> None:
        self._path    = "/sys/class/power_supply/BAT"+str(no)
        self._internals = {
            "params"        : lambda : self._params,
            "health"        : lambda : f"{int(self.charge_full)*100 // int(self.charge_full_design)}%",
            "all_stats"     : lambda : "\n".join([f"{key} : {self._get(key)}" for key in self._params]+[f"health : {self.health}"])
        }
        self._params = []

        for f in ls(self._path):
            if isfile(self._path + "/" + f) and f!= "uevent":
                self._params.append(f)

        self._params.sort()
    
    def _get(self, name):
        op = 0

        if name in self._internals:
            return self._internals[name]()
        else:
            try:
                with open (f"{self._path}/{name}", 'r') as batt:
                    op = batt.read().strip()
            except Exception as e:
                raise RuntimeError(f"{op} not accessible, is unreadable or insufficient permissions.") from e
            finally:
                return op
    
    def __str__(self) -> str:
        data = [
            f"   Battery Information",
            f"-----------------------",
            f"Date         : {datetime.now().date()}",
            f"Time         : {str(datetime.now().time()).split('.')[0]}",
            f"Capacity     : {self.capacity}",
            f"Charge Now   : {self.charge_now}",
            f"Charge Full  : {self.charge_full}",
        ]

        return "\n".join(data)
    
    def __getattr__(self, name: str):
        op = 0
        try:
            if name in self._params or name in self._internals:
                op = self._get(name)
            else:
                raise AttributeError(f"Battery does not contain {name}")
        except Exception as e:
            print(e)
        finally:
            return op            

if __name__ == "__main__":            
    print(_Battery().all_stats)
