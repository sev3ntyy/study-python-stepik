class LightSwitch:
    def __init__(self):
        self._is_on = False
    def toggle(self):
        if self._is_on == False:
            self._is_on = True
        else:
            self._is_on = False
    def is_on(self):
        return self._is_on



class Secret:
    def __init__(self, secret_message: str):
        self._message = secret_message

    def get_message(self) -> str:
        return self._message

class User:
    def __init__(self):
        self._age = 0 
    def get_age(self):
        return self._age
    def set_age(self, new_age):
        if not isinstance(new_age, int) or new_age <= 0:
            return self._age
        else:
            self._age = new_age

class Thermostat:
    def __init__(self, temp):
        self._temperature = temp
    def get_temperature(self):
        return self._temperature
    def set_temperature(self, new_temp):
        if 0 <= new_temp <= 100:
            self._temperature = new_temp






