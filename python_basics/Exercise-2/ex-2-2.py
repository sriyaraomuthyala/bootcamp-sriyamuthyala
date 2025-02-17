from ex-2-1 import Employee

class Manager(Employee):
    def __init__(self, name, emp_id, position, subordinates=None):
        super().__init__(name, emp_id, position)
        self.subordinates = subordinates if subordinates else []
    
    def add_subordinate(self, employee):
        self.subordinates.append(employee)
    
    def list_subordinates(self):
        return [emp.display_info() for emp in self.subordinates]
