"""
    Welcome to Dice Roller a simple luck game
    How to play? very easy:
        -Choose how much dices do you want to play with
        -The programme will generate the wanted amount of dices with different numbers
        -The AI will choose the same amount of dices but with different numbers since the numbers ar random
        -And simply like that if you're luck and the total of your dices bigger than the AI you'll win
        -And vice versa
    Note: Don't enter a negative value or a number bigger than 100
"""


import math , random
from typing import Dict
from Types import Score, Dice, Nums
from Utils import print_title, print_formated_text, get_scores, number_validation, print_results


def print_rules() -> None:
    """
    Printing the game title and rules
    :return: None
    """
    print_title(title=f"DICE ROLLER")
    print_formated_text(messages=f"""Welcome to Dice Roller a simple luck game
    How to play? very easy:
        -Choose how much dices do you want to play with
        -The programme will generate the wanted amount of dices with different numbers
        -The AI will choose the same amount of dices but with different numbers since the numbers ar random
        -And simply like that if you're luck and the total of your dices bigger than the AI you'll win
        -And vice versa
    Note: Don't enter a negative value or a number bigger than 100""")


def get_dice_dict() -> Dict[int,Dice]:
    """
    Get the dict of dices
    :return: a dict with int keys for indexing and a Dice type value representing the display of dices
    """

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
    """
    Get the wanted amount of dices from the user
    :return: an int value representing the number of dices
    """

    #Get a validate number of dices
    num_of_dices = number_validation(prompt=f"Enter how many dices do you want (Between 1 and 100):")

    #Return the number of dices
    return num_of_dices


def get_dices_nums(num_of_dices: int) -> Nums:
    """
    Get a random value between 1 and 6 for each die
    :param num_of_dices: an int param representing the number of the dices
    :return: a Nums type representing the generated random values
    """

    #Return the list of random values for each die
    return  random.choices(range(1,7),k=num_of_dices)


def print_dices(num_of_dices: int,dice_nums: Nums,num_of_dices_in_row: int = 4) -> None:
    """
    Print the chosen amount of dices
    :param num_of_dices: an integer param representing the number of dices
    :param dice_nums: a Nums type param representing the random values of dices
    :param num_of_dices_in_row: an integer param representing the number of dices in each row. The default value is 4
    :return: None
    """

    #Get the dices dict
    dice_dict = get_dice_dict()
    #Caculate the number of rows
    num_of_dices_rows = math.ceil(num_of_dices / num_of_dices_in_row)
    #Get the number of lines in one die
    num_of_dices_lines = len(dice_dict[1])

    #Print the dices
    for i in range(num_of_dices_rows):
        #Get the numbers of the start and end dices for each row to the end of the dices
        start , end = i * num_of_dices_in_row, min((i + 1) * num_of_dices_in_row,num_of_dices)

        #print each die of the current row line by line
        for line in range(num_of_dices_lines):
            print(" ".join(dice_dict[dice_nums[die]][line] for die in range(start, end)))
        print()


def roll_and_print_dices(num_of_dices: int, player_name: str) -> int:
    """
        Roll dices, get there random values, print them, calculate and return the total of them
        :param num_of_dices: an integer representing the entered number of dices
        :param player_name: a string representing the current player
        :return: an integer representing the total of random values
    """
    print_formated_text(messages=f"{player_name} dices", option="upper")
    # Get the player
    player_dices = get_dices_nums(num_of_dices=num_of_dices)
    # Print player dices
    print_dices(num_of_dices=num_of_dices, dice_nums=player_dices)
    # the total of random values then return it
    return sum(player_dices)


def get_results(num_of_player_dices: int, scores: Score) -> None:
    """
    Get the result of the game
    :param num_of_player_dices: an integer param representing the entered number of the dices
    :param scores: a Score type param representing each score with his value
    :return: None
    """

    #Player Dices
    player_total = roll_and_print_dices(num_of_dices=num_of_player_dices,player_name="User")
    #AI Dices
    ai_total = roll_and_print_dices(num_of_dices=num_of_player_dices,player_name="AI")

    #Print result text and update scores
    print_results(player_1_result=player_total,player_2_result=ai_total,scores=scores)

    #Print totals
    print_formated_text(messages=[f"Your total: {player_total}",f"AI total: {ai_total}"])


def start_game(scores: Score) -> None:
    """
    Starting the game one time
    :param scores: a Score type param representing each score with his value
    :return: None
    """
    #Print game title and rules
    print_rules()
    #Get the entered amount of dices
    num_of_player_dices = get_player_num_of_dices()
    #Get game results
    get_results(num_of_player_dices=num_of_player_dices, scores=scores)


def main() -> None:
    """
    The main function of the programme
    :return: None
    """

    #Init scores
    scores = dict(player_score=0, ai_score=0)

    #Run the game n time
    while True:
        #Run the game
        start_game(scores=scores)
        #Stop the game if the user choose that
        if input(f"Press anything to play again or q to quit: ").lower() == "q":
            #Get the final scores
            get_scores(scores=scores)
            #Print a goodbye message
            print_formated_text(messages=f"GoodBye! See You later")
            break


if __name__ == "__main__":
    main()