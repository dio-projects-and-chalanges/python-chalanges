from desafios.sistema_bancario.contracts.transaction_interface import TransactionInterface
from desafios.sistema_bancario.entities.account import Account


class Customer:
    def __init__(self, address: str, accounts: list):
        self._address = address
        self._accounts = accounts

    @property
    def address(self):
        return self._address
    
    @property
    def accounts(self):
        return self._accounts
    
    def make_transaction(self, account: Account, transaction: TransactionInterface):
        pass

    def create_account(self, account: Account):
        pass