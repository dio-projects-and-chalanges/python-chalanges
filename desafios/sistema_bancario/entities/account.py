from __future__ import annotations
from desafios.sistema_bancario.entities.customer import Customer
from desafios.sistema_bancario.entities.history import History


class Account:
    def __init__(self, number: int, agency: str, client: Customer, balance: float):
        self._number = number
        self._agency = agency
        self._client = client
        self._balance = balance
        self._history = list[History] = []

    @property
    def balance(self):
        return self._balance
    
    @property
    def number(self):
        return self._number
    
    @property
    def agency(self):
        return self._agency
    
    @property
    def client(self):
        return self._client
    
    @property
    def history(self):
        return self._history
    
    def new_account(self, client: Customer, number: int) -> Account:
        pass
    
    def withdraw(self, value: float) -> bool:
        pass
    
    def deposit(self, value: float) -> bool:
        pass
    
    def get_balance(self):
        pass
    
    def show_history(self):
        pass