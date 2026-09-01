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

