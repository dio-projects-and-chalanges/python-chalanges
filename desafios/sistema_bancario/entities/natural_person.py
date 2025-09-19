from datetime import date
from desafios.sistema_bancario.entities.customer import Customer


class NaturalPerson(Customer):
    def __init__(self, address, accounts, cpf: str, name: str, birthdate: date):
        super().__init__(address, accounts)
        self._cpf = cpf
        self._name = name
        self._birthdate = birthdate


    @property
    def cpf(self):
        return self._cpf

    @property
    def name(self):
        return self._name
    
    @property
    def birthdate(self):
        return self._birthdate