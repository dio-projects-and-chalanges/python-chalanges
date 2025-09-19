from desafios.sistema_bancario.entities.account import Account


class CheckingAccount(Account):
    def __init__(self, number, agency, client, balance, limit: float, withdrawal_limit: int):
        super().__init__(number, agency, client, balance)
        self._limit = limit
        self._withdrawal_limit = withdrawal_limit
        self._withdrawals_made = 0

    @property
    def limit(self) -> float:
        return self._limit

    @property
    def withdrawal_limit(self) -> int:
        return self._withdrawal_limit
