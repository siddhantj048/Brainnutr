from typing import Union, Tuple
import os


class Auth:
    _path = "users/"

    def __init__(self) -> None:
        "Checks if users folder exists. Creates a new one if it isn't there"
        if not os.path.exists(self._path):
            os.mkdir(self._path)

    def register(self, username: str, password: str, data: Union[list, dict, None]={"streak": 0}) -> bool:
        if not os.path.isfile(f"{self._path}{username}.txt"):
            with open(f"{self._path}{username}.txt", "w") as fp:
                fp.write(password + "\n")
                fp.write(str(data))
            return True
        return False
    

    def login(self, username: str, password: str) -> Tuple[bool, Union[list, dict, None]]:
        if not os.path.isfile(f"{self._path}{username}.txt"):
            return False, None
        
        with open(f"{self._path}{username}.txt", "r") as fp:
            pwd, data = fp.read().split("\n")
            if pwd == password:
                return True, eval(data)
            else:
                return False, None
    

    def get_all_data(self) -> dict:
        temp = {}
        for file in os.listdir(self._path):
            with open(f"{self._path}{file}", "r") as fp:
                pwd, data = fp.read().split("\n")


            username = file[0:-4]
            temp[username] = [pwd, eval(data)]
        return temp
    

    def set_data(self, username: str, data: Union[list, dict, None]) -> None:
        with open(f"{self._path}{username}.txt", "r") as fp:
            pwd = fp.read().split("\n")[0]
    
        with open(f"{self._path}{username}.txt", "w") as fp:
            fp.write(f"{pwd}\n"+ str(data))
        
    def get_data(self, username: str) -> Union[list, dict, None]:
        with open(f"{self._path}{username}.txt", "r") as fp:
            _, data = fp.read().split("\n")
        return eval(data)