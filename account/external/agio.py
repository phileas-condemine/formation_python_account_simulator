from datetime import datetime, timedelta
from typing import Union, Optional



from ..internal import BankAccount

class AgiosBankAccount(BankAccount):
    def __init__(self,owner: str,initial_balance: int,bank: BankAccount):
        super().__init__(owner, initial_balance)
        self.__bank:BankAccount = bank
        self.__date_passage_negatif:Optional[datetime] = None
    
    def _credit(self,value: int, transaction_date: datetime = datetime.now()):
        self._balance += value
        montant_agio = self.__check_for_agios(transaction_date)
        if montant_agio > 0:
            print(f"paiement d'un agio d'un montant de {montant_agio}")
            self.__date_passage_negatif = None
            super().transfer_to(self.__bank, montant_agio, transaction_date)
    
    def transfer_to(self, recipient: "BankAccount", value : int, transaction_date: datetime = datetime.now()):
        if self._balance < value and self.__date_passage_negatif is None:
            self.__date_passage_negatif = transaction_date
        
        super().transfer_to(recipient, value, transaction_date)

        

    def __check_for_agios(self, transaction_date: datetime = datetime.now()) -> int:
        if self.__date_passage_negatif is not None:
            montant_agio = transaction_date - self.__date_passage_negatif
            return montant_agio.days
        else:
            return 0
            
