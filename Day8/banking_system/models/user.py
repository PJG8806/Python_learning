import account as Account

class User:
    #사용자 이름 및 계좌 정보 초기화
    def username(self, username : str) -> None:
        self.username = username
        self.account = Account()