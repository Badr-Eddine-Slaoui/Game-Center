import random , time


def get_params() -> tuple[tuple[str,str,str],dict[str,int]]:
    return (
        ("rock", "paper", "scissors"),
        {
            "player_score": 0,
            "ai_score": 0
        }
    )


def print_menu() -> None:
    print("┌────────── ROCK PAPER SCISSORS ──────────┐")
    print("        Welcome Rock Paper Scissors        ")
    print("└─────────────────────────────────────────┘")


def get_player_choice(options: tuple[str,str,str]) -> str:
    while True:
        print("┌─────────────────────────────────────────┐")
        print("                YOUR TURN!!                ")
        print("└─────────────────────────────────────────┘")

        choice = input("Enter a choice (rock, paper, scissors) or use emojis: ")
        choice = "rock" if choice == "✊" else "paper" if choice == "🖐" else "scissors" if choice == "✌" else choice.lower()
        if choice in options:
            break

        print("┌─────────────────────────────────────────┐")
        print("              Invalid choice!!             ")
        print("└─────────────────────────────────────────┘")

    print("┌─────────────────────────────────────────┐")
    print(f"             You Chose: {choice}          ")
    print("└─────────────────────────────────────────┘")
    return choice


def get_ai_choice(options: tuple[str, str, str]) -> str:
    print("┌─────────────────────────────────────────┐")
    print("                 AI TURN!!                 ")
    print("└─────────────────────────────────────────┘")
    time.sleep(1)
    choice = random.choice(options)
    print("┌─────────────────────────────────────────┐")
    print(f"              AI Chose: {choice}          ")
    print("└─────────────────────────────────────────┘")

    return choice


def get_results(player_choice: str, ai_choice: str, scores: dict[str,int]) -> None:
    if player_choice == ai_choice:
        print("┌─────────────────────────────────────────┐")
        print("               It's a tie!!                ")
        print("└─────────────────────────────────────────┘")
    elif (player_choice == "rock" and ai_choice == "scissors") or (player_choice == "scissors" and ai_choice == "paper") or (
            player_choice == "paper" and ai_choice == "rock"):
        print("┌─────────────────────────────────────────┐")
        print("                 You win!!                 ")
        print("└─────────────────────────────────────────┘")
        scores.update(player_score=scores.get("player_score") + 1)
    else:
        print("┌─────────────────────────────────────────┐")
        print("                You lost!!                 ")
        print("└─────────────────────────────────────────┘")
        scores.update(ai_score=scores.get("ai_score") + 1)


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
    player_choice = get_player_choice(options=get_params()[0])
    ai_choice = get_ai_choice(options=get_params()[0])

    get_results(player_choice=player_choice, ai_choice=ai_choice, scores=scores)


def main(scores: dict[str, int] = None) -> None:
    if scores is None:
        scores = get_params()[1]
    while True:
        start_game(scores=scores)
        if input("Press anything to play again or q to quit: ").lower() == "q":
            get_scores(scores=scores)
            print("┌─────────────────────────────────────────┐")
            print("          GoodBye! See You later           ")
            print("└─────────────────────────────────────────┘")
            break


if __name__ == "__main__":
    main()