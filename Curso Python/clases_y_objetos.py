class Person:
    def __init__(self, first_name, last_name, CI):
        self.first_name = first_name
        self.last_name = last_name
        self.CI = CI

    def full_info(self):
        return f"Hola {self.first_name} {self.last_name} tu cedula es: {self.CI}"
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
class Employee(Person):
    def __init__(self, first_name, last_name, CI, salary):
        super().__init__(first_name, last_name, CI)
        self.salary = salary
    
    def lab_info(self):
        return f"Hola trabajador {super().full_name()} tu salario actual es: {self.salary}$"


person_jordy = Person('Jordy','Ortiz','2450938722')
employee_jordy = Employee('Jordy','Ortiz','2450938722', '750')

print(person_jordy.full_info())
print(employee_jordy.full_info())
print(employee_jordy.lab_info())