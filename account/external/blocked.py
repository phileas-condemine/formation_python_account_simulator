from datetime import datetime, timedelta
from typing import Union, Optional


from ..internal import BankAccount

class InsufficientBalance(ValueError): 
    pass


class BlockedBankAccount(BankAccount):
    def transfer_to(self, recipient: BankAccount, value: int, transaction_date: datetime = datetime.now()):
        # Il vaut mieux commencer par éliminer les cas d'erreur avant de continuer
        if self._balance < value:
            raise InsufficientBalance(f"Solde {self._balance} de compte insuffisant pour une transaction de {value} from {self.name} to {recipient.name}")
        super().transfer_to(recipient, value, transaction_date)


