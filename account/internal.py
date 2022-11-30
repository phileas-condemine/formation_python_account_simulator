from datetime import datetime, timedelta
from typing import Union, Optional



class BankAccount():
    def __init__(self,owner: str,initial_balance: int):
        self.__name: str = owner
        self._balance: int = initial_balance
        
    def __str__(self):
        return f'{self.__name} a un solde courant de {self._balance}€'
    
    def _credit(self, value: int, transaction_date: datetime):
        if value > 0:
            self._balance += value
        else : 
            raise ValueError(f'La valeur à transférer devrait être positive, elle vaut {value}')

    current_balance = property(fget=lambda self: self._balance)

    
    def transfer_to(self, recipient: "BankAccount", value : int, transaction_date: datetime = datetime.now()):
        """
        Makes a money transfer from the current account to the recipient

        Args:
            recipient (BankAccount): _description_
            value (int): _description_
            transaction_date (datetime, optional): _description_. Defaults to datetime.now().
        """
        recipient._credit(value,transaction_date)
        self._balance -= value
        
    def name_getter(self):
        return self.__name
    
    def name_setter(self,value:str):
        self.__name = value
    
    #name = property(fget = (lambda self: self.__name), fset= (lambda self, value: self.__name = value), doc = "Propriétaire du compte banquaire")
    name = property(fget = name_getter, fset= name_setter, doc = "Propriétaire du compte banquaire")
