import banking_system.models.user as User
import banking_system.utils.exceptions as UserNotFoundError

class BankingService:
    #사용자 목록 초기화 생성자
    def __init__(self) -> None:
        self.users = []

    #사용자 추가 매서드
    def add_user(self, username : str) -> None:
        self.users.append(User(username))

    #사용자 찾아주는 매서드
    def find_user(self, username : str) -> User:
        for i in self.users:
            if i == username:
                return i
        raise UserNotFoundError(username)

    #사용자 매뉴 제공 메서드
    def user_menu(self, username : str) -> None:
        user = self.find_user(username)
        while True:
            choice = input("원하는 작업을 입력해주세요(1: 입금, 2: 출금, 3: 잔고 확인, 4: 거래 내역, 5: 종료")
            match choice:
                case "1":
                    amount = int(input("입금 금액을 입력해주세요: "))
                    user.account.deposit(amount)
                case "2":
                    amount = int(input("입금 금액을 입력해주세요: "))
                    user.account.withdraw(amount)
                case "3":
                    print(f"현재 잔고는: {user.account.get_balance()}")
                case "4":
                    for i in user.account.get_transactions():
                        print(i)
                case "5":
                    break