class Person:
    def __init__(self, first_name, last_name, CI):
        self.first_name = first_name
        self.last_name = last_name
        self.CI = CI

    def full_info(self):
        return f"Hola {self.first_name} {self.last_name} tu cedula es: {self.CI}"
    

person_jordy = Person('Jordy','Ortiz','2450938722')
print(person_jordy.full_info())