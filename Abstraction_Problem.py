class Employee:
    
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
        
    def get_salary(self):
        return self.base_salary + (self.base_salary * 0.2)
    
emp1 = Employee("Muhammad Shariq", 50000)
print(emp1.get_salary())