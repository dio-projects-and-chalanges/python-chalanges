from desafios.sistema_bancario.contracts.transaction_interface import TransactionInterface


class Deposit(TransactionInterface):
    def __init__(self, value: float):
        self._value = value

    @property
    def value(self):
        return self._value
    
    def register():
        pass