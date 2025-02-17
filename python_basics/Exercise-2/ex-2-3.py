from ex-2-1 import Employee

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = {}
    
    def add_employee(self, employee, salary):
        self.employees[employee] = salary
    
    def total_salary(self):
        return sum(self.employees.values())
    
    def list_employees(self):
        return [f"{emp.display_info()}, Salary: {self.employees[emp]}" for emp in self.employees]
