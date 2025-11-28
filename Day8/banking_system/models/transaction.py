class Transaction:
    #거래정보 초기화
    def __init__(self, transaction_type : str, amount : int, balance : str) -> None:
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance
    
    #거래정보 반환
    def __str__(self) -> str:
        return f"{self.transaction_type} 금액: {self.amount} 잔고: {self.balance}"
    
    #거래정보 튜플 반환
    def to_tuple(self) -> tuple:
        return (self.transaction_type, self.amount, self.balance)