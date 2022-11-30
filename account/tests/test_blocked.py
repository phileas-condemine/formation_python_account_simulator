from datetime import datetime, timedelta
from typing import Union, Optional
from formation_python_account_simulator.account.external.agio import AgiosBankAccount
from formation_python_account_simulator.account.external.blocked import BlockedBankAccount, InsufficientBalance
from formation_python_account_simulator.account.internal import BankAccount
import pytest

def test_match():
    with pytest.raises(InsufficientBalance):
        billy = BlockedBankAccount("billy", 200)
        johnny = BlockedBankAccount("johnny", 100)
        billy.transfer_to(johnny,500,datetime(2022,11,29))

