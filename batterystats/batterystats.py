from os import listdir as ls
from os.path import isfile, exists
from datetime import datetime

class Battery:
    """
    A class for reading Battery 
    related parameters in realtime.

    ...

    Attributes
    ----------
    _path : str
        stores the path to read the values from
        (defaults to -> /sys/class/power_supply/BAT0 )
    
    params : list
        list of available readable parameters of the selected Battery
    
    
    Properties
    ----------
    health : int
        Get the health of the battery based on the percentage change of
        Actual Max Charge over Designed Max charge
    
    all_stats : dict
        Get all the statistics as a dicitonary


    Methods
    -------
    _get(name):
        Gets the value of that specific parameter which is requested.
    """
    def __init__(self, no=0) -> None:
        '''
        __init__ method to create Battery Object

        @param no :
            The Battery Number to create object of. Defaults to 0.
        '''
        self._path    = "/sys/class/power_supply/BAT"+str(no)

        if not exists(self._path):
            self._path = "/sys/class/power_supply/AC"

        self.params = []

        for f in ls(self._path):
            if isfile(self._path + "/" + f) and f!= "uevent":
                self.params.append(f)

        self.params.sort()
    @property
    def date(self) -> str:
        return str(datetime.now().date())
    
    @property
    def time(self) -> str:
        return str(datetime.now().time()).split('.')[0]

    @property
    def health(self) -> int:
        '''
        Get the health of the battery
        '''
        return int(self.charge_full)*100 // int(self.charge_full_design)
    
    @property
    def all_stats(self) -> dict:
        '''
        Get all the Statistical parameters of the battery, as a dictionary
        '''
        data = {key : self._get(key) for key in self.params}
        data["health"] = self.health
        return data

    def _get(self, name) -> int:
        '''
        Get the value of the parameter from the specific file

        @param name:
            The name of the parameter needs to be exactly same as the parameter name.
        '''
        op = 0
        
        try:
            with open (f"{self._path}/{name}", 'r') as batt:
                op = batt.read().strip()
        except Exception as e:
            raise RuntimeError(f"{op} not accessible, is unreadable or insufficient permissions.") from e
        finally:
            return op
    
    def __str__(self) -> str:
        return \
            f"          Battery Information           \n"   \
            f"----------------------------------------\n"   \
            f"Date - Time  : {self.date} | {self.time}\n"   \
            f"Battery Path : {self._path}\n"                \
            f"Status       : {self.status}\n"               \
            f"Capacity     : {self.capacity}%\n"            \
            f"Charge Now   : {self.charge_now}\n"           \
            f"Charge Full  : {self.charge_full}\n" 

    
    def __getattr__(self, name: str):
        op = 0
        try:
            if name in self.params:
                op = self._get(name)
            else:
                raise AttributeError(f"Battery does not contain {name}")
        except Exception as e:
            print(e)
        finally:
            return op            

if __name__ == "__main__":            
    print(Battery().all_stats)
