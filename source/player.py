def pon():
    while True:
        choice = input("じゃんけんの手を入力してください（1: グー, 2: チョキ, 3: パー）: ")
        if choice in ['1', '2', '3']:
            if choice == '1':
                return "グー"
            elif choice == '2':
                return "チョキ"
            elif choice == '3':
                return "パー"
        else:
            print("無効な入力です。1, 2, 3のいずれかを入力してください。")


player_choice = pon()
print(f"プレイヤーの手: {player_choice}")
