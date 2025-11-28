from typing import Callable
#함수 타입을 표시해주는거

def validate_transaction(func: Callable) -> Callable:
    def wrapper(self, amount : int) -> None:
        if amount <= 0:
            raise ValueError("0보다 커야합니다.")
        return func(self, amount)
    return wrapper