class Employee:
    def __init__(self, name, emp_id, position):
        self.name = name
        self.emp_id = emp_id
        self.position = position
    
    def update_position(self, new_position):
        self.position = new_position
    
    def display_info(self):
        return f"Employee: {self.name}, ID: {self.emp_id}, Position: {self.position}"
    
    def __str__(self):
        return f"Employee(Name: {self.name}, ID: {self.emp_id}, Position: {self.position})"
    
    def __repr__(self):
        return self.__str__()
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, new_position):
        self._position = new_position
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
