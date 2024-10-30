"""
    Welcome to Rock Paper Scissors a simple luck game
    I guess everyone knows how to play but in case u don't know:
        -Choose one option ("rock", "paper", "scissors")
        -The AI will also pick one
        _Case of winning:
            +If you chose "rock" and AI chose "scissors"
            +If you chose "scissors" and AI chose "paper"
            +If you chose "paper" and AI chose "rock"
        _And vice versa
        -If you both chose the same option it's a tie
    Note: you can use emojis
"""


import random , time
from Utils import print_title, print_formated_text, get_scores
from Types import Option, Score


def print_rules() -> None:
    """
    Printing the game title and rules
    :return: None
    """

    #Print game title
    print_title(title=f"Rock Paper Scissors")
    #Print game rules
    print_formated_text(messages=f"""
    Welcome to Rock Paper Scissors a simple luck game
    I guess everyone knows how to play but in case u don't know:
        -Choose one option ("rock", "paper", "scissors")
        -The AI will also pick one
        _Case of winning:
            +If you chose "rock" and AI chose "scissors"
            +If you chose "scissors" and AI chose "paper"
            +If you chose "paper" and AI chose "rock"
        _And vice versa 
        -If you both chose the same option it's a tie
    Note: you cane use emojis
""")


def get_player_choice(options: Option) -> str:
    """
    Get the player choice, print it and return it
    :param options: an Option type param representing the game's options
    :return: a strig representing the chosen choice
    """
    #Player turn
    print_formated_text(messages=f"Your turn",option="upper")

    #Get a valid choice from player
    while True:
        choice = input(f"Enter a choice (rock, paper, scissors) or use emojis: ")
        #Turn emojis to words if player use them
        choice = "rock" if choice == "✊" else ("paper" if choice == "🖐" else ("scissors" if choice == "✌" else choice.lower()))
        #Stop the loop after getting a valid choice
        if choice in options:
            break
        #Print a message if it's not
        print_formated_text(messages=f"Invalid choice!!")

    #Print player choice
    print_formated_text(messages=f"You Chose: {choice}")
    #Return the player choice
    return choice


def get_ai_choice(options: Option) -> str:
    """
    Get the AI choice, print it and return it
    :param options: an Option type param representing the game's options
    :return: a strig representing the chosen choice
    """

    #AI turn
    print_formated_text(messages=f"Ai turn!!",option="upper")
    #Sleep for 1 sec to give the effect of choosing
    time.sleep(1)
    #Get a random choice of game choices
    choice = random.choice(options)
    #Print AI choice
    print_formated_text(messages=f"AI Chose: {choice}")
    #Return it
    return choice


def get_results(player_choice: str, ai_choice: str, scores: Score) -> None:
    """
    Get the results and print them
    :param player_choice: a string representing the player choice
    :param ai_choice: a string representing the AI choice
    :param scores: a Score type param representing each score with his value
    :return: None
    """
    #Init the winning cases
    winning_cases = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    #Get the result
    if player_choice == ai_choice:
        result=f"It's a tie!!"
    elif winning_cases[player_choice] == ai_choice:
        result=f"You win!!"
        scores["player_score"] += 1
    else:
        result=f"You lost!!"
        scores["ai_score"] += 1
    #Print the result
    print_formated_text(messages=result)


def start_game(scores: Score) -> None:
    """
        Starting the game one time
        :param scores: a Score type param representing each score with his value
        :return: None
        """

    # Print game title and rules
    print_rules()
    #Init game's options
    options = "rock", "paper", "scissors"
    #Get player choice
    player_choice = get_player_choice(options=options)
    #Get AI choice
    ai_choice = get_ai_choice(options=options)
    #Print the results
    get_results(player_choice=player_choice, ai_choice=ai_choice, scores=scores)


def main() -> None:
    """
    The main function of the programme
    :return: None
    """

    # Init scores
    scores = dict(player_score=0, ai_score=0)

    # Run the game n time
    while True:
        # Run the game
        start_game(scores=scores)
        # Stop the game if the user choose that
        if input(f"Press anything to play again or q to quit: ").lower() == "q":
            #Get and print the final scores
            get_scores(scores=scores)
            #Print a goodbye message
            print_formated_text(messages=f"GoodBye! See You later")
            #stop the game
            break


if __name__ == "__main__":
    main()