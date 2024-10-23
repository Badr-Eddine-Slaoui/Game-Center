import random


def get_params() -> dict[str,int]:
    return {
            "player_score": 0,
            "ai_score": 0
        }


def print_menu() -> None:
    print("┌────────────── PYTHON SLOTS ──────────────┐")
    print("     Symbols:🍉 │ ⭐ │ 🍋 │ 🔔 │ 🍒        ")
    print("└──────────────────────────────────────────┘")


def get_balance() -> int:
    while True:
        balance = input("Enter your balance: ")
        if not balance.isdigit():
            print("┌──────────────────────────────────────────┐")
            print("        Please enter a valid number         ")
            print("└──────────────────────────────────────────┘")
            continue

        balance = int(balance)

        if balance < 100:
            print("┌──────────────────────────────────────────┐")
            print("     Balance must be greater than 100       ")
            print("└──────────────────────────────────────────┘")
            continue
        else:
            break
    return balance


def get_bet(balance: int) -> int:
    while True:
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("┌──────────────────────────────────────────┐")
            print("        Please enter a valid number         ")
            print("└──────────────────────────────────────────┘")
            continue

        bet = int(bet)

        if bet > balance:
            print("┌──────────────────────────────────────────┐")
            print("            Insufficient funds              ")
            print("└──────────────────────────────────────────┘")
            continue

        if bet <= 0:
            print("┌──────────────────────────────────────────┐")
            print("     Balance must be greater than zero      ")
            print("└──────────────────────────────────────────┘")
            continue
        else:
            break
    return bet


def print_current_balance(balance: int) -> None:
    print("┌──────────────────────────────────────────┐")
    print(f"        Current balance: ${balance:,.2f}           ")
    print("└──────────────────────────────────────────┘")


def spin_row() -> list[str]:
    print("┌──────────────────────────────────────────┐")
    print("               Spinning...                  ")
    print("└──────────────────────────────────────────┘")

    symbols = ["🍉", "⭐", "🍋", "🔔", "🍒"]
    return [random.choice(symbols) for _ in range(3)]


def print_row(row: list[str]) -> None:
    print("┌──────────────────────────────────────────┐")
    print("          │  ", "  │  ".join(row), "  │          ")
    print("└──────────────────────────────────────────┘")


def get_payout(row: list[str], bet: int,scores: dict[str,int]) -> int:
    payout = 0
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            payout = bet * 2
            scores.update(player_score=scores.get("player_score") + 3)
        elif row[0] == "🍉":
            payout = bet * 4
            scores.update(player_score=scores.get("player_score") + 6)
        elif row[0] == "🍋":
            payout = bet * 6
            scores.update(player_score=scores.get("player_score") + 9)
        elif row[0] == "🔔":
            payout = bet * 8
            scores.update(player_score=scores.get("player_score") + 12)
        elif row[0] == "⭐":
            payout = bet * 10
            scores.update(player_score=scores.get("player_score") + 15)

    elif row[0] == row[1] or row[0] == row[2] or row[1] == row[2]:
        index_of_def = 2 if row[0] == row[1] else 1 if row[0] == row[2] else 0
        index_of_same = 2 if index_of_def == 1 else 1 if index_of_def == 0 else 1
        if row[index_of_same] == "🍒":
            scores.update(player_score=scores.get("player_score") + 2)
        elif row[index_of_same] == "🍉":
            scores.update(player_score=scores.get("player_score") + 4)
        elif row[index_of_same] == "🍋":
            scores.update(player_score=scores.get("player_score") + 6)
        elif row[index_of_same] == "🔔":
            scores.update(player_score=scores.get("player_score") + 8)
        elif row[index_of_same] == "⭐":
            scores.update(player_score=scores.get("player_score") + 10)

        if row[index_of_def] == "🍒":
            scores.update(ai_score=scores.get("ai_score") + 1)
        elif row[index_of_def] == "🍉":
            scores.update(ai_score=scores.get("ai_score") + 2)
        elif row[index_of_def] == "🍋":
            scores.update(ai_score=scores.get("ai_score") + 3)
        elif row[index_of_def] == "🔔":
            scores.update(ai_score=scores.get("ai_score") + 4)
        elif row[index_of_def] == "⭐":
            scores.update(ai_score=scores.get("ai_score") + 5)

    else:
        scores.update(ai_score=scores.get("ai_score") + 1)

    if payout > 0:
        print("┌──────────────────────────────────────────┐")
        print(f"         Congrats you won a ${payout:,.2f}!!             ")
        print("└──────────────────────────────────────────┘")
    else:
        print("┌──────────────────────────────────────────┐")
        print("       Sorry you lost this round!!          ")
        print("└──────────────────────────────────────────┘")
    return payout


def print_result(balance: int) -> None:
    if balance > 0:
        print("┌──────────────────────────────────────────┐")
        print(f"   Game over! You finale balance is ${balance:,.2f}")
        print("└──────────────────────────────────────────┘")
    else:
        print("┌──────────────────────────────────────────┐")
        print("       Game over! You Lost Everything       ")
        print("└──────────────────────────────────────────┘")


def get_scores(scores: dict[str,int]) -> None:
    if scores.get("player_score") == scores.get("ai_score"):
        print("┌─────────────────────────────────────────┐")
        print("           Wow! It's a tie!!               ")
        print("└─────────────────────────────────────────┘")
    elif scores.get("player_score") > scores.get("ai_score"):
        print("┌─────────────────────────────────────────┐")
        print("         Congratulation! You win!!         ")
        print("└─────────────────────────────────────────┘")
    else:
        print("┌─────────────────────────────────────────┐")
        print("            Hard luck you lost!!           ")
        print("└─────────────────────────────────────────┘")

    print("┌─────────────────────────────────────────┐")
    print(f"              Your score: {scores.get('player_score')}            ")
    print(f"               AI score: {scores.get('ai_score')}            ")
    print("└─────────────────────────────────────────┘")


def start_game(scores: dict[str,int]) -> None:
    print_menu()

    balance = get_balance()

    while True:
        print_current_balance(balance=balance)

        bet = get_bet(balance=balance)
        balance -= bet

        row = spin_row()

        print_row(row=row)

        payout = get_payout(row=row, bet=bet, scores=scores)

        balance += payout

        if balance <= 0:
            break

        if input("Do you want to spin again? (Y/N): ").upper() == "N":
            break

    print_result(balance=balance)


def main(scores: dict[str, int] = None) -> None:
    if scores is None:
        scores = get_params()
    while True:
        start_game(scores=scores)
        if input("Press anything to play again or q to quit: ").lower() == "q":
            get_scores(scores=scores)
            print("┌──────────────────────────────────────────┐")
            print("           GoodBye! See You later           ")
            print("└──────────────────────────────────────────┘")
            break


if __name__ == "__main__":
    main()