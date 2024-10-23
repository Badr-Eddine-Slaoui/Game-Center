import math , random , time


def get_params() -> dict[str,int]:
    return {
            "player_score": 0,
            "ai_score": 0
        }


def print_menu() -> None:
    print("┌───────────── GUESS THE SUM ─────────────┐")
    print("          Welcome To Guess The Sum         ")
    print("└─────────────────────────────────────────┘")


def get_num_of_numbers() -> int:
    while True:
        num_of_nums = input("Enter the number of positive number you wanna enter\n"
                           "The AI will generate the same amount of numbers\n"
                           "Try to guess the total of the numbers entered by the AI\n"
                           "He will try to guess the some of yours\n"
                           "Whoever gets the correct sum in the fewest attempts win: ")
        if not num_of_nums.isdigit():
            print("┌─────────────────────────────────────────┐")
            print("            Enter a valid number!          ")
            print("└─────────────────────────────────────────┘")
            continue

        num_of_nums = int(num_of_nums)

        if num_of_nums <= 0:
            print("┌─────────────────────────────────────────┐")
            print("            Enter a valid number!          ")
            print("└─────────────────────────────────────────┘")
            continue
        if num_of_nums > 100:
            print("┌─────────────────────────────────────────┐")
            print("             Too many numbers!             ")
            print("└─────────────────────────────────────────┘")
            continue
        break
    return num_of_nums


def get_player_numbers(num_of_numbers: int) -> list[int]:
    print("┌─────────────────────────────────────────┐")
    print("       Warning: if you entered a null      ")
    print("          negative or a non number         ")
    print("            we'll EXCLUDE them!!           ")
    print("└─────────────────────────────────────────┘")

    player_numbers = []

    for i in range(num_of_numbers):
        while True:
            num = input(f"Enter {i + 1} number (Between 1 and 100): ")
            if not num.isdigit():
                print("┌─────────────────────────────────────────┐")
                print("            Enter a valid number!          ")
                print("└─────────────────────────────────────────┘")
                continue

            num = int(num)

            if num > 100:
                print("┌─────────────────────────────────────────┐")
                print("              Number Too Big!              ")
                print("└─────────────────────────────────────────┘")
                continue

            player_numbers.append(num)
            break

    return player_numbers


def get_ai_numbers(num_of_numbers: int) -> list[int]:
    ai_numbers = []

    for i in range(num_of_numbers):
        num = random.randint(1,100)
        ai_numbers.append(num)

    return ai_numbers


def filter_numbers_list(numbers_list: list[int]) -> list[int]:
    return [num for num in numbers_list if 0 < num <= 100]


def get_player_guesses(numbers_list: list[int]) -> int:
    sum_of_numbers = sum(numbers_list)
    start = (sum_of_numbers - 1) // 20 * 20 + 1
    end = start + 19
    sum_range = [start, end]

    print("┌─────────────────────────────────────────┐")
    print("               Start Guessing              ")
    print("└─────────────────────────────────────────┘")

    attempts_count = 1

    while True:
        while True:
            guess = input(f"Guess {attempts_count} the sum is between {sum_range}: ")
            if not guess.isdigit():
                print("┌─────────────────────────────────────────┐")
                print("            Enter a valid number!          ")
                print("└─────────────────────────────────────────┘")
                continue

            guess = int(guess)

            if guess <= 0:
                print("┌─────────────────────────────────────────┐")
                print("            Enter a valid number!          ")
                print("└─────────────────────────────────────────┘")
                continue

            if guess > end or guess < start:
                print("┌─────────────────────────────────────────┐")
                print("     Enter a number in the given range     ")
                print("└─────────────────────────────────────────┘")
                continue

            break

        if guess == sum_of_numbers:
            break
        elif guess > sum_of_numbers:
            print("┌─────────────────────────────────────────┐")
            print("              Number's too big!            ")
            print("└─────────────────────────────────────────┘")
        else:
            print("┌─────────────────────────────────────────┐")
            print("             Number's too small!           ")
            print("└─────────────────────────────────────────┘")

        attempts_count += 1

    return attempts_count


def get_ai_guesses(numbers_list: list[int]) -> int:
    sum_of_numbers = sum(numbers_list)
    start = (sum_of_numbers - 1) // 20 * 20 + 1
    end = start + 19

    attempts_count = 1

    print("┌─────────────────────────────────────────┐")
    print("             AI Guessing........           ")
    print("└─────────────────────────────────────────┘")

    guess = math.floor((end + start) / 2)

    while True:
        if guess == sum_of_numbers:
            break
        elif guess > sum_of_numbers:
            end = guess
        else:
            start = guess
        attempts_count += 1

        guess = random.randint(start, end)

    time.sleep(2 if attempts_count < 10 else attempts_count - 6)
    return attempts_count


def get_results(player_attempts_count: int, ai_attempts_count: int, scores: dict[str,int]) -> None:

    if player_attempts_count == ai_attempts_count:
        print("┌─────────────────────────────────────────┐")
        print("               It's a tie!!                ")
        print("└─────────────────────────────────────────┘")

    elif player_attempts_count < ai_attempts_count:
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
    print(f"       Your total of attempts: {player_attempts_count}        ")
    print(f"        AI total of attempts: {ai_attempts_count}         ")
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


def start_game(scores: dict[str,int]) -> None:
    print_menu()
    num_of_nums = get_num_of_numbers()

    player_numbers = filter_numbers_list(numbers_list=get_player_numbers(num_of_numbers=num_of_nums))
    ai_numbers = get_ai_numbers(num_of_numbers=num_of_nums)

    player_attempts_count = get_player_guesses(numbers_list=ai_numbers)
    ai_attempts_count = get_ai_guesses(numbers_list=player_numbers)

    get_results(player_attempts_count=player_attempts_count, ai_attempts_count=ai_attempts_count, scores=scores)


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