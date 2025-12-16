class Person:
    variable_global = 0
    def __init__(self, first_name, last_name, CI):
        self.first_name = first_name
        self.last_name = last_name
        self.CI = CI

    def full_info(self):
        return f"Hola {self.first_name} {self.last_name} tu cedula es: {self.CI}"
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    @classmethod
    def counter_increment(cls):
        cls.variable_global += 2
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Employee(Person):
    def __init__(self, first_name, last_name, CI, salary):
        super().__init__(first_name, last_name, CI)
        self.salary = salary
    
    def lab_info(self):
        return f"Hola trabajador {super().full_name()} tu salario actual es: {self.salary}$"

class Functions():
    @staticmethod
    def saludo(first_name):
        return f'Hola {first_name} Como estas?'

person_jordy = Person('Jordy','Ortiz','2450938722')
employee_jordy = Employee('Jordy','Ortiz','2450938722', '750')

print(person_jordy.full_info())
print(Functions.saludo(person_jordy))
print(employee_jordy.full_info())
print(employee_jordy.lab_info())
print(Person.variable_global)
Person.counter_increment()
print(Person.variable_global)