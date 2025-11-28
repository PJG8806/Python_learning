import banking_system.models.transaction as Transaction
import banking_system.utils.exceptions as NegativeAmountError
import banking_system.utils.decorators as validate_transaction

class Account:
    bank_name = "은행"
    #거래 내역 리스트 및 계좌 잔고 초기화
    def __init__(self) -> None:
        self.__balance = 0
        self.transactions = []

    #입금 매서드
    @validate_transaction
    def deposit(self, amount : int) -> None:
        if amount < 0:
            raise NegativeAmountError()
        self.__balance += amount
        self.transactions.append(Transaction("입금", amount, self.__balance))

    #출금 매서드
    @validate_transaction
    def withdraw(self, amount : int) -> None:
        if amount < 0:
            raise NegativeAmountError()
        self.__balance -= amount
        self.transactions.append(Transaction("출금", amount, self.__balance))

    #잔고 반환 매서드
    def get_balance(self) -> int:
        return self.__balance
    
    #거래 내역 반환 매서드
    def get_transactions(self) -> list:
        return self.transactions
    
    #
    def get_bank_name(cls) -> str:
        return cls.bank_name

    def set_bank_name(cls, name : str) -> None:
        cls.bank_name = name