from ex-2-1 import Employee
from ex-2-3 import Department

class Project:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.employees = []
    
    def assign_employee(self, employee):
        self.employees.append(employee)
    
    def list_employees(self):
        return [emp.display_info() for emp in self.employees]
