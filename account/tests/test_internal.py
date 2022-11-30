from datetime import datetime, timedelta
from typing import Union, Optional
from formation_python_account_simulator.account.external.agio import AgiosBankAccount
from formation_python_account_simulator.account.external.blocked import BlockedBankAccount, InsufficientBalance
from formation_python_account_simulator.account.internal import BankAccount

def test_money_transfer():
    billy = BankAccount("billy", 10000)
    johnny = BankAccount("johnny", 5000)
    billy.transfer_to(johnny,1000,datetime(2022,11,29))
    assert billy.current_balance == 9000 and johnny.current_balance == 6000

