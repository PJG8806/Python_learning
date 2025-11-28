class InsufficientFundsError():
    def __init__(self, balance : int) -> None:
        super.__init__(f"잔액이 부족합니다. 잔액: {balance}")
class NegativeAmountError():
    def __init__(self) -> None:
        super.__init__("음수 금액은 안됩니다.")
class UserNotFoundError():
    def __init__(self, username : str) -> None:
        super.__init__(f"사용자: {username} 찾을수 없습니다.")