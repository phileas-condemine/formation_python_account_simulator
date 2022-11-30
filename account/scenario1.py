from datetime import datetime, timedelta
from typing import Union, Optional
from formation_python_account_simulator.account.external.agio import AgiosBankAccount
from formation_python_account_simulator.account.external.blocked import BlockedBankAccount, InsufficientBalance
from formation_python_account_simulator.account.internal import BankAccount



bank = BankAccount("LCL", 10000)
walmart = BankAccount("Walmart", 5000)
alice = BankAccount("Alice Worz", 500)
bob = BankAccount("Bob Müller", 100)

str(bank)


{key:str(value) for key,value in globals().items() if isinstance(value,BankAccount)}

alice.transfer_to(walmart,100)
bob.transfer_to(walmart,100)
alice.transfer_to(bob,100)
bob.transfer_to(walmart,200)

print({key:str(value) for key,value in globals().items() if isinstance(value,BankAccount)})


type(ValueError)
type(BankAccount)


    
    
bank = BankAccount("LCL", 10000)
walmart = BankAccount("Walmart", 5000)
alice = BankAccount("Alice Worz", 500)
bob = BlockedBankAccount("Bob Müller", 100)

str(bank)


{key:str(value) for key,value in globals().items() if isinstance(value,BankAccount)}

try:
    alice.transfer_to(walmart,100)
    bob.transfer_to(walmart,100)
    alice.transfer_to(bob,100)
    bob.transfer_to(walmart,200)
except InsufficientBalance as e:
    print(str(e))


{key:str(value) for key,value in globals().items() if isinstance(value,BankAccount)}

bank = BankAccount("LCL", 10000)
walmart = BankAccount("Walmart", 5000)
alice = BankAccount("Alice Worz", 500)
bob = AgiosBankAccount("Bob Müller", 100, bank)


str(bank)

{key:str(value) for key,value in globals().items() if isinstance(value,BankAccount)}

try:
    alice.transfer_to(walmart,100, datetime.now())
    bob.transfer_to(walmart,100, datetime.now())
    alice.transfer_to(bob,100, datetime.now())
    bob.transfer_to(walmart,200, datetime.now())
    {key:str(value) for key,value in globals().items() if isinstance(value,BankAccount)}
    new_date = datetime.now() + timedelta(days=5)
    alice.transfer_to(bob,10,transaction_date= new_date)
    {key:str(value) for key,value in globals().items() if isinstance(value,BankAccount)}


except InsufficientBalance as e:
    print(str(e))


print({key:str(value) for key,value in globals().items() if isinstance(value,BankAccount)})
