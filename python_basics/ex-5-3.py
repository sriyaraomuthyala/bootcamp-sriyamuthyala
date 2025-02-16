class Temperature:
    def __init__(self, temp):
        self._temp = None
        self.temp = temp
    
    @property
    def temp(self):
        return self._temp
    
    @temp.setter
    def temp(self, value):
        if -273.15 <= value <= 5000:
            self._temp = value
        else:
            raise ValueError("Temperature out of range")
