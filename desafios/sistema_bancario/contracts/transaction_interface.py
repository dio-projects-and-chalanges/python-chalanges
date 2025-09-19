from abc import ABC, abstractmethod

from desafios.sistema_bancario.entities.account import Account


class TransactionInterface(ABC):
        
    @abstractmethod
    def register(self, account: Account):
        """Inicia uma transação"""
        pass