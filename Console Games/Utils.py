"""
    This file contain all the helper and utils for all the games
"""


from Types import  Score
from typing import Optional, List, Tuple


def print_formated_text(messages: str | List[str], option: Optional[str] = None) -> None:
    """
    Print games messages in the format theme
    :param messages: a string or list of strings param representing a message or more.
    :param option: an Optional param representing the letters form, default value is None.
    :return: None
    """

    # Check the validity of the values of the param option
    if option not in {None, "upper", "lower", "capital"}:
        raise ValueError("The 'option' parameter must be 'upper', 'lower', 'capital' or None.")

    # Check if the type is a string
    if isinstance(messages, str):
        # If it is split message lines to get an array of messages
        messages = messages.splitlines()

    # Init the array that will contain all formatted messages
    formatted_messages = []
    # Map the messages array
    for message in messages:
        # Apply the specified option to each message
        formatted_message = {
            None: message,
            "upper": message.upper(),
            "lower": message.lower(),
            "capital": message.capitalize()
        }[option]
        # Append the formatted message to the formatted messages array
        formatted_messages.append(f"{' ' * 4}{formatted_message}{' ' * 4}\n")
    # Determine the maximum length of formatted messages.
    max_len = max(len(msg) for msg in formatted_messages)

    # The top and bottom of the message format
    top = f"┌{'─' * (max_len - 2)}┐"
    bottom = f"└{'─' * (max_len - 2)}┘"
    # Print the final result
    print(f"{top}\n{''.join(formatted_messages)}{bottom}")


def print_title(title: str) -> None:
    """
        Print games titles in the format theme
        :param title: a string param representing the title.
        :return: None
        """

    # The top of the title format
    top = f"┌{'─'*11} {title.upper()} {'─'*11}┐"
    # Change the title format
    middle = f"{' ' * 7}Welcome To {title.capitalize()}{' ' * 8}"
    # The bottom of the title format
    bottom = f"└{'─' * (len(middle) - 2)}┘"
    # Print the final result
    print(f"{top}\n{middle}\n{bottom}")


def get_scores(scores: Score) -> None:
    """
    Get results and print the final scores
    :param scores: a Score type param representing each score with his value
    :return: None
    """

    #Check the results
    if scores["player_score"] == scores["ai_score"]:
        result = "Wow! It's a tie!!"
    elif scores["player_score"] > scores["ai_score"]:
        result = "Congratulation! You win!!"
    else:
        result = "Hard luck you lost!!"
    #Print results
    print_formated_text(messages=result)
    #Print the final scores
    print_formated_text(messages=[f"Your score: {scores['player_score']}",f"AI score: {scores['ai_score']}"])


def number_validation(prompt: str, min_val: int = 1, max_val: int = 100) -> int :
    """
    Get a valid number for games
    :param prompt: a string param representing the input prompt
    :param min_val: an integer param representing the min value for the number
    :param max_val: an integer param representing the max value for the number
    :return:
    """
    while True:
        # Get the number value
        num = input(prompt)

        # Check if the entered value is empty
        if num == "":
            print_formated_text(messages=f"Please enter a number!")
            continue

        # Check if the entered value is a digit
        if not num.isdigit():
            print_formated_text(messages=f"Enter a valid number!")
            continue

        # Convert the validated input value to an integer
        num = int(num)

        # Check if the entered number is a valid number for the game rules
        if num < min_val or num > max_val:
            print_formated_text(messages=f"Enter a number in the given range")
            continue
        # Stop the loop after getting a valid number
        break

    #Return the validated number
    return num


def calculate_range(number: int) -> Tuple[int,int]:
    """
    Calculate the range of a given number
    :param number: an integer param representing the given number
    :return: a Tuple representing the range of the number
    """

    #Calculate the end and start of the range
    start = (number - 1) // 20 * 20 + 1
    end = start + 19
    #Return the range
    return  start,end


def print_results(player_1_result: int, player_2_result: int, scores: Score) -> None:
    """
    Compare the results of two player, update scores and print the results
    :param player_1_result: an integer param representing the result of the first player
    :param player_2_result: an integer param representing the result of the second player
    :param scores: a Score type param representing each score with his value
    :return: None
    """

    #Compare the results of the two players and
    if player_1_result == player_2_result:
        result = f"It's a tie!!"
    elif player_1_result > player_2_result:
        result = f"You win!!"
        #Update player score
        scores["player_score"] += 1
    else:
        result = f"You lost!!"
        #Update ai score
        scores["ai_score"] += 1

    #Print the final result
    print_formated_text(messages=result)