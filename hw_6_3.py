class Worker:
    def __init__(self, name, surname, position, income : dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self,full_name):
        return f'Доход {full_name}: {sum(self._income.values())}р. в месяц'


worker_1 = Position(name='Ivan',
                    surname='Pupkin',
                    position='Engineer',
                    income={"wage": 20000, "bonus": 15000})
print(worker_1.get_total_income(worker_1.get_full_name()))



