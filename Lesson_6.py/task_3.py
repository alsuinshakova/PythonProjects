# Solution:


class Worker:

    def __init__(self, name='Александр', surname='Морозов', position='инженер', wage=120, bonus=50):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return self._income['wage'] + self._income['bonus']


v_pet = Position('Александр', 'Морозов', 'главный инженер', 150, 60)
print(f'New attributes are: {v_pet.name}, {v_pet.surname}, {v_pet.position}, {v_pet._income}')
print(f'Total salary of {v_pet.get_full_name()} is {v_pet.get_full_salary()}')
