import random , time


def get_params() -> tuple[list[str],list[int],list[int],dict[int,list[int]],dict[str,int]]:
    return (["┌─────┐─────┌─────┐",
             "│     │     │     │",
             "│─────┘─────└─────│",
             "│     │     │     │",
             "│─────┐─────┌─────│",
             "│     │     │     │",
             "└─────┘─────└─────┘"],
            [3, 9, 15],
            [1, 3, 5],
            {
                1: [],
                3: [],
                5: []
            },
            {
                "player_score": 0,
                "ai_score": 0
            }
    )


def print_menu() -> None:
    print("┌────────────── TIC TAC TOE ──────────────┐")
    print("           Welcome To Tic Tac Toe          ")
    print("└─────────────────────────────────────────┘")


def get_symbols() -> tuple[str,str]:
    symbol = ""
    ai_symbol = ""
    while True:
        symbol = input("Choose you symbol (X/O): ").upper()
        if symbol == "O":
            ai_symbol = "X"
            break
        elif symbol == "X":
            ai_symbol = "O"
            break
        else:
            print("┌─────────────────────────────────────────┐")
            print("        Invalid choice! Choose X or O      ")
            print("└─────────────────────────────────────────┘")
            continue
    return symbol, ai_symbol


def player_turn(y_indexes: list[int], x_indexes: list[int], chosen_spots: dict[int,list[int]],
                      screen: list[str], player_symbol: str) -> None:
    while True:
        print("┌─────────────────────────────────────────┐")
        print("                YOUR TURN!!                ")
        print("└─────────────────────────────────────────┘")
        while True:
            player_y_choice = input("Enter slot line number (1,2,3): ")
            if not player_y_choice.isdigit():
                print("┌─────────────────────────────────────────┐")
                print("      Invalid choice! Choose 1,2 or 3      ")
                print("└─────────────────────────────────────────┘")
                continue
            player_y_choice = int(player_y_choice)
            if player_y_choice < 0 or player_y_choice > 3:
                print("┌─────────────────────────────────────────┐")
                print("      Invalid choice! Choose 1,2 or 3      ")
                print("└─────────────────────────────────────────┘")
                continue
            player_y_choice = y_indexes[player_y_choice - 1]
            break

        while True:
            player_x_choice = input("Enter slot number (1,2,3): ")
            if not player_x_choice.isdigit():
                print("┌─────────────────────────────────────────┐")
                print("      Invalid choice! Choose 1,2 or 3      ")
                print("└─────────────────────────────────────────┘")
                continue
            player_x_choice = int(player_x_choice)
            if player_x_choice < 0 or player_x_choice > 3:
                print("┌─────────────────────────────────────────┐")
                print("      Invalid choice! Choose 1,2 or 3      ")
                print("└─────────────────────────────────────────┘")
                continue
            player_x_choice = x_indexes[player_x_choice - 1]
            break

        if player_x_choice in chosen_spots.get(player_y_choice):
            print("┌─────────────────────────────────────────┐")
            print("        This slot is already taken!!       ")
            print("└─────────────────────────────────────────┘")
            continue
        else:
            chosen_spots.get(player_y_choice).append(player_x_choice)
            new_line = list(screen[player_y_choice])
            new_line[player_x_choice] = player_symbol
            screen[player_y_choice] = "".join(new_line)
            time.sleep(1)
            print_screen(screen=screen)
            break


def ai_turn(y_indexes: list[int], x_indexes: list[int], chosen_spots: dict[int,list[int]],
                      screen: list[str], ai_symbol: str) -> None:
    print("┌─────────────────────────────────────────┐")
    print("                 AI TURN!!                 ")
    print("└─────────────────────────────────────────┘")
    player_symbol = "O" if ai_symbol == "X" else "X"
    line_one = list(screen[1])
    line_two = list(screen[3])
    line_three = list(screen[5])

    if (line_one[9] == line_one[15] == ai_symbol or
        line_two[3] == line_three[3] == ai_symbol or
        line_two[9] == line_three[15] == ai_symbol) and 3 not in chosen_spots.get(1):
        line_one[3] = ai_symbol
        screen[1] = "".join(line_one)
        chosen_spots.get(1).append(3)

    elif (line_one[3] == line_one[15] == ai_symbol or
        line_two[9] == line_three[9] == ai_symbol) and 9 not in chosen_spots.get(1):
        line_one[9] = ai_symbol
        screen[1] = "".join(line_one)
        chosen_spots.get(1).append(9)

    elif(line_one[3] == line_one[9] == ai_symbol or
        line_two[15] == line_three[15] == ai_symbol or
        line_two[9] == line_three[3] == ai_symbol) and 15 not in chosen_spots.get(1):
        line_one[15] = ai_symbol
        screen[1] = "".join(line_one)
        chosen_spots.get(1).append(15)

    elif (line_two[9] == line_two[15] == ai_symbol or
        line_one[3] == line_three[3] == ai_symbol) and 3 not in chosen_spots.get(3):
        line_two[3] = ai_symbol
        screen[3] = "".join(line_two)
        chosen_spots.get(3).append(3)

    elif (line_two[3] == line_two[15] == ai_symbol or
        line_one[9] == line_three[9] == ai_symbol or
        line_one[15] == line_three[3] == ai_symbol or
        line_one[3] == line_three[15] == ai_symbol) and 9 not in chosen_spots.get(3):
        line_two[9] = ai_symbol
        screen[3] = "".join(line_two)
        chosen_spots.get(3).append(9)

    elif(line_two[3] == line_two[9] == ai_symbol or
        line_one[15] == line_three[15] == ai_symbol) and 15 not in chosen_spots.get(3):
        line_two[15] = ai_symbol
        screen[3] = "".join(line_two)
        chosen_spots.get(3).append(15)

    elif (line_three[9] == line_three[15] == ai_symbol or
        line_two[3] == line_one[3] == ai_symbol or
        line_two[9] == line_one[15] == ai_symbol) and 3 not in chosen_spots.get(5):
        line_three[3] = ai_symbol
        screen[5] = "".join(line_three)
        chosen_spots.get(5).append(3)

    elif (line_three[3] == line_three[15] == ai_symbol or
        line_two[9] == line_one[9] == ai_symbol) and 9 not in chosen_spots.get(5):
        line_three[9] = ai_symbol
        screen[5] = "".join(line_three)
        chosen_spots.get(5).append(9)

    elif(line_three[3] == line_three[9] == ai_symbol or
        line_two[15] == line_one[15] == ai_symbol or
        line_two[9] == line_one[3] == ai_symbol) and 15 not in chosen_spots.get(5):
        line_three[15] = ai_symbol
        screen[5] = "".join(line_three)
        chosen_spots.get(5).append(15)

    elif (line_one[9] == line_one[15] == player_symbol or
        line_two[3] == line_three[3] == player_symbol or
        line_two[9] == line_three[15] == player_symbol) and 3 not in chosen_spots.get(1):
        line_one[3] = ai_symbol
        screen[1] = "".join(line_one)
        chosen_spots.get(1).append(3)

    elif (line_one[3] == line_one[15] == player_symbol or
        line_two[9] == line_three[9] == player_symbol) and 9 not in chosen_spots.get(1):
        line_one[9] = ai_symbol
        screen[1] = "".join(line_one)
        chosen_spots.get(1).append(9)

    elif(line_one[3] == line_one[9] == player_symbol or
        line_two[15] == line_three[15] == player_symbol or
        line_two[9] == line_three[3] == player_symbol) and 15 not in chosen_spots.get(1):
        line_one[15] = ai_symbol
        screen[1] = "".join(line_one)
        chosen_spots.get(1).append(15)

    elif (line_two[9] == line_two[15] == player_symbol or
        line_one[3] == line_three[3] == player_symbol) and 3 not in chosen_spots.get(3):
        line_two[3] = ai_symbol
        screen[3] = "".join(line_two)
        chosen_spots.get(3).append(3)

    elif (line_two[3] == line_two[15] == player_symbol or
        line_one[9] == line_three[9] == player_symbol or
        line_one[15] == line_three[3] == player_symbol or
        line_one[3] == line_three[15] == player_symbol) and 9 not in chosen_spots.get(3):
        line_two[9] = ai_symbol
        screen[3] = "".join(line_two)
        chosen_spots.get(3).append(9)

    elif(line_two[3] == line_two[9] == player_symbol or
        line_one[15] == line_three[15] == player_symbol) and 15 not in chosen_spots.get(3):
        line_two[15] = ai_symbol
        screen[3] = "".join(line_two)
        chosen_spots.get(3).append(15)

    elif (line_three[9] == line_three[15] == player_symbol or
        line_two[3] == line_one[3] == player_symbol or
        line_two[9] == line_one[15] == player_symbol) and 3 not in chosen_spots.get(5):
        line_three[3] = ai_symbol
        screen[5] = "".join(line_three)
        chosen_spots.get(5).append(3)

    elif (line_three[3] == line_three[15] == player_symbol or
        line_two[9] == line_one[9] == player_symbol) and 9 not in chosen_spots.get(5):
        line_three[9] = ai_symbol
        screen[5] = "".join(line_three)
        chosen_spots.get(5).append(9)

    elif(line_three[3] == line_three[9] == player_symbol or
        line_two[15] == line_one[15] == player_symbol or
        line_two[9] == line_one[3] == player_symbol) and 15 not in chosen_spots.get(5):
        line_three[15] = ai_symbol
        screen[5] = "".join(line_three)
        chosen_spots.get(5).append(15)

    else:
        while True:
            ai_x_choice = random.choice(x_indexes)
            ai_y_choice = random.choice(y_indexes)
            if ai_x_choice not in chosen_spots.get(ai_y_choice):
                new_line = list(screen[ai_y_choice])
                new_line[ai_x_choice] = ai_symbol
                screen[ai_y_choice] = "".join(new_line)
                chosen_spots.get(ai_y_choice).append(ai_x_choice)
                break

    time.sleep(1)
    print_screen(screen=screen)


def print_screen(screen: list[str]) -> None:
    for line in screen:
        print(line)


def check_results(screen: list[str],chosen_spots: dict[int,list[int]],player_symbol: str, ai_symbol: str,
                  game_running: bool, scores: dict[str,int]) -> bool:
    line_one = list(screen[1])
    line_two = list(screen[3])
    line_three = list(screen[5])
    if (line_one[3] == line_one[9] == line_one[15] == player_symbol or
        line_two[3] == line_two[9] == line_two[15] == player_symbol or
        line_three[3] == line_three[9] == line_three[15] == player_symbol or
        line_one[3] == line_two[3] == line_three[3] == player_symbol or
        line_one[9] == line_two[9] == line_three[9] == player_symbol or
        line_one[15] == line_two[15] == line_three[15] == player_symbol or
        line_one[3] == line_two[9] == line_three[15] == player_symbol or
        line_one[15] == line_two[9] == line_three[3] == player_symbol):
        print("┌─────────────────────────────────────────┐")
        print("            Congrats! You Win!!!           ")
        print("└─────────────────────────────────────────┘")
        scores.update(player_score=scores.get("player_score") + 1)
        game_running = False

    elif (line_one[3] == line_one[9] == line_one[15] == ai_symbol or
        line_two[3] == line_two[9] == line_two[15] == ai_symbol or
        line_three[3] == line_three[9] == line_three[15] == ai_symbol or
        line_one[3] == line_two[3] == line_three[3] == ai_symbol or
        line_one[9] == line_two[9] == line_three[9] == ai_symbol or
        line_one[15] == line_two[15] == line_three[15] == ai_symbol or
        line_one[3] == line_two[9] == line_three[15] == ai_symbol or
        line_one[15] == line_two[9] == line_three[3] == ai_symbol):
        print("┌─────────────────────────────────────────┐")
        print("           Game Over! You lost!!           ")
        print("└─────────────────────────────────────────┘")
        scores.update(ai_score=scores.get("ai_score") + 1)
        game_running = False

    else:
        if len(chosen_spots.get(1)) == len(chosen_spots.get(3)) == len(chosen_spots.get(5)) == 3:
            print("┌─────────────────────────────────────────┐")
            print("          Game Over! It's a Tie!!          ")
            print("└─────────────────────────────────────────┘")
            game_running = False

    return game_running

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
    params = get_params()
    screen = params[0]
    x_indexes = params[1]
    y_indexes = params[2]
    chosen_spots = params[3]

    print_menu()

    symbols = get_symbols()
    player_symbol = symbols[0]
    ai_symbol = symbols[1]

    game_running = True

    while game_running:
        player_turn(y_indexes=y_indexes, x_indexes=x_indexes, chosen_spots=chosen_spots, screen=screen,
                          player_symbol=player_symbol)

        game_running = check_results(screen=screen, chosen_spots=chosen_spots, player_symbol=player_symbol,
                                     ai_symbol=ai_symbol,
                                     game_running=game_running,scores=scores)

        if not game_running:
            break

        ai_turn(y_indexes=y_indexes, x_indexes=x_indexes, chosen_spots=chosen_spots, screen=screen,
                      ai_symbol=ai_symbol)

        game_running = check_results(screen=screen, chosen_spots=chosen_spots, player_symbol=player_symbol,
                                     ai_symbol=ai_symbol,
                                     game_running=game_running,scores=scores)


def main(scores: dict[str, int] = None) -> None:
    if scores is None:
        scores = get_params()[4]

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