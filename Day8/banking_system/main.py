import banking_system.models.banking_service as BankingService

def main() -> None:
    service = BankingService()
    while True:
        choic = input("모드를 입력해주세요(1: 사용자 추가, 2: 사용자 찾기(입출고 내역), 3: 종료")
        match choic:
            case "1":
                username = input("사용자 이름을 입력해주세요")
                service.add_user(username)
            case "2":
                username = input("찾을 사용자 이름을 입력해주세요")
                service.user_menu(service.find_user(username))                    
            case "3":
                print("종료합니다")
                break


if __name__ == "__main__":
    main()