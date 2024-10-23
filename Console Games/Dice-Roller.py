import math , random

def get_params() -> dict[str,int]:
    return {
            "player_score": 0,
            "ai_score": 0
        }


def print_menu() -> None:
    print("┌────────────── DICE ROLLER ──────────────┐")
    print("           Welcome To Dice Roller          ")
    print("└─────────────────────────────────────────┘")


def get_dice_dict() -> dict[int,tuple[str,str,str,str,str]]:
    return {
        1: ("┌─────────┐",
            "│         │" ,
            "│    ●    │" ,
            "│         │" ,
            "└─────────┘"),
        2: ("┌─────────┐",
            "│  ●      │" ,
            "│         │" ,
            "│      ●  │" ,
            "└─────────┘"),
        3: ("┌─────────┐",
            "│  ●      │" ,
            "│    ●    │" ,
            "│      ●  │" ,
            "└─────────┘"),
        4: ("┌─────────┐",
            "│  ●   ●  │" ,
            "│         │" ,
            "│  ●   ●  │" ,
            "└─────────┘"),
        5: ("┌─────────┐",
            "│  ●   ●  │" ,
            "│    ●    │" ,
            "│  ●   ●  │" ,
            "└─────────┘"),
        6: ("┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘")
    }


def get_player_num_of_dices() -> int:
    while True:
        num_of_dices = input("Enter how many dice you want the ai will choose the same number\n"
                            "Who have the biggest total win: ")
        if not num_of_dices.isdigit():
            print("┌─────────────────────────────────────────┐")
            print("            Enter a valid number!          ")
            print("└─────────────────────────────────────────┘")
            continue

        num_of_dices = int(num_of_dices)

        if num_of_dices <= 0:
            print("┌─────────────────────────────────────────┐")
            print("            Enter a valid number!          ")
            print("└─────────────────────────────────────────┘")
            continue
        if num_of_dices > 100:
            print("┌─────────────────────────────────────────┐")
            print("               Too many dices!             ")
            print("└─────────────────────────────────────────┘")
            continue

        break
    return num_of_dices


def get_dices(num_of_dice: int):
    dice = []
    for die in range(num_of_dice):
        dice.append(random.randint(1, 6))
    return dice


def print_dices(num_of_dice: int,dice: list[int]):
    dice_dict = get_dice_dict()
    num_of_dice_in_row = 4
    num_of_dice_rows = math.ceil(num_of_dice / num_of_dice_in_row)
    num_of_dice_lines = len(dice_dict.get(1))

    for i in range(num_of_dice_rows):
        start = i * num_of_dice_in_row
        end = (i + 1) * num_of_dice_in_row
        if end > num_of_dice:
            end = num_of_dice
        for line in range(num_of_dice_lines):
            for die in range(start, end):
                print(dice_dict.get(dice[die])[line], end=" ")
            print()
        print(end="")


def get_total(dice: list[int]):
    total = 0
    for die in dice:
        total += die
    return total


def get_results(num_of_player_dices: int, scores: dict[str,int]) -> None:
    num_of_ai_dices = num_of_player_dices

    print("┌─────────────────────────────────────────┐")
    print("                 YOUR DICES                ")
    print("└─────────────────────────────────────────┘")
    player_dices = get_dices(num_of_dice=num_of_player_dices)
    print_dices(num_of_dice=num_of_player_dices, dice=player_dices)
    player_total = get_total(player_dices)

    print("┌─────────────────────────────────────────┐")
    print("                  AI DICES                 ")
    print("└─────────────────────────────────────────┘")
    ai_dices = get_dices(num_of_dice=num_of_ai_dices)
    print_dices(num_of_dice=num_of_ai_dices, dice=ai_dices)
    ai_total = get_total(ai_dices)

    if player_total == ai_total:
        print("┌─────────────────────────────────────────┐")
        print("               It's a tie!!                ")
        print("└─────────────────────────────────────────┘")

    elif player_total > ai_total:
        print("┌─────────────────────────────────────────┐")
        print("                 You win!!                 ")
        print("└─────────────────────────────────────────┘")
        scores.update(player_score=scores.get("player_score") + 1)

    else:
        print("┌─────────────────────────────────────────┐")
        print("                You lost!!                 ")
        print("└─────────────────────────────────────────┘")
        scores.update(ai_score=scores.get("ai_score") + 1)

    print("┌─────────────────────────────────────────┐")
    print(f"              Your total: {player_total}            ")
    print(f"               AI total: {ai_total}            ")
    print("└─────────────────────────────────────────┘")


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


def start_game(scores: dict[str,int]):
    print_menu()
    num_of_player_dices = get_player_num_of_dices()
    get_results(num_of_player_dices=num_of_player_dices, scores=scores)


def main(scores: dict[str, int] = None) -> None:
    if scores is None:
        scores = get_params()
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