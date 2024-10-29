"""
    Welcome to Guess The Sum a simple luck game
    How to play? very easy:
        -Choose how much numbers do you want to play with
        -Then enter the values of your numbers
        -The AI will choose the same amount of numbers but with different values since the numbers ar random
        _Then you'll need to guess the sum of AI numbers, and he'll guess yours
        -And simply like that, whoever gets the correct sum in the fewest attempts win
    Note: Don't enter a negative value or numbers bigger than 100
"""


import math , random , time
from Utils import print_title, print_formated_text, get_scores, number_validation, calculate_range, print_results
from Types import Score, Nums


def print_rules() -> None:
    """
    Printing the game title and rules
    :return: None
    """
    print_title(title=f"Guess The Sum")
    print_formated_text(messages=f"""
    Welcome to Guess The Sum a simple luck game
    How to play? very easy:
        -Choose how much numbers do you want to play with
        -Then enter the values of your numbers
        -The AI will choose the same amount of numbers but with different values since the numbers ar random
        _Then you'll need to guess the sum of AI numbers, and he'll guess yours 
        -And simply like that, whoever gets the correct sum in the fewest attempts win
    Note: Don't enter a negative value or numbers bigger than 100
""")


def get_num_of_values() -> int:
    """
    Get the wanted amount of numbers from the user
    :return: an int value representing the amount of numbers
    """
    # Return the validated number of values
    return number_validation(prompt=f"Enter the amount of positive number you want (Between 1 and 100): ")


def get_player_numbers(num_of_vals: int) -> Nums:
    """
    Get the values of player numbers
    :param num_of_vals: an integer representing the entered amount of values
    :return: a Nums type representing the list of values
    """

    #Get list of validated numbers values from player
    player_numbers = [number_validation(prompt=f"Enter {i + 1} number (Between 1 and 100): ") for i in range(num_of_vals)]

    #Return the list of numbers
    return player_numbers


def get_ai_numbers(num_of_vals: int) -> Nums:
    """
        Get the random values of AI numbers
        :param num_of_vals: an integer representing the entered amount of values
        :return: a Nums type representing the list of values
    """
    #return a list of values between 1 and 100
    return random.choices(range(1,101),k=num_of_vals)


def get_player_guesses(numbers_list: Nums) -> int:
    """
    Get the player guesses and return the attempt count
    :param numbers_list: a Nums type represent the AI numbers list
    :return: an integer representing the count of the player attempts
    """

    #Calculate the sum of AI numbers list
    sum_of_numbers = sum(numbers_list)
    #Calculate the start and the end of the sum range
    start, end = calculate_range(number=sum_of_numbers)
    sum_range = [start, end]

    #The start of guessing
    print_formated_text(messages=f"Start Guessing")

    #Init the player attempts count by 1
    attempts_count = 1

    #The guessing loop
    while True:
        #Get a validated guess
        guess = number_validation(prompt=f"Guess {attempts_count} the sum is between {sum_range}: ",min_val=start,max_val=end)

        #Stop the loop after getting the right guess
        if guess == sum_of_numbers:
            break
        elif guess > sum_of_numbers:
            hint=f"Number's too big!"
        else:
            hint=f"Number's too small!"
        # Print a hint message if it's not
        print_formated_text(messages=hint)

        #Increment player attempts count by 1
        attempts_count += 1

    #Return the player attempts count
    return attempts_count


def get_ai_guesses(numbers_list: Nums) -> int:
    """
    Get the player guesses, print them and return the attempt count
    :param numbers_list: a Nums type represent the player numbers list
    :return: an integer representing the count of the AI attempts
    """

    # Calculate the sum of AI numbers list
    sum_of_numbers = sum(numbers_list)
    # Calculate the start and the end of the sum range
    start, end = calculate_range(number=sum_of_numbers)

    #Init AI attempts count by 1
    attempts_count = 1

    #Start of AI guessing
    print_formated_text(messages=f"AI Guessing....")

    #Init the first guess by the middle of the range to make guessing more accurate
    guess = (end + start) // 2

    #Guessing loop
    while True:
        # Sleep for 1 sec to give the effect of the AI guessing the sum
        time.sleep(1)
        #Print the AI guess
        print_formated_text(messages=f"Attempts {attempts_count}: {guess}")

        #Stop the loop after getting the right guess
        if guess == sum_of_numbers:
            break
        #If the guess is bigger than the sum assign it to the end of the range so the AI don't guess a bigger number again
        elif guess > sum_of_numbers:
            end = guess
        #If the guess is smaller than the sum assign it to the start of the range so the AI don't guess a smaller number again
        else:
            start = guess
        #Increment AI attempts count by 1
        attempts_count += 1

        # assign the middle of the new range to make guessing more accurate
        guess = (end + start) // 2

    #Return AI attempts count
    return attempts_count


def get_results(player_attempts_count: int, ai_attempts_count: int, scores: Score) -> None:
    """
    Get and print the result of the game
    :param player_attempts_count: an integer param representing the player attempts count
    :param ai_attempts_count: an integer param representing the AI attempts count
    :param scores: a Score type param representing scores with their values
    :return: None
    """

    #Print the results message and update scores
    print_results(player_1_result=ai_attempts_count,player_2_result=player_attempts_count,scores=scores)

    #Print attempts count for both player and AI
    print_formated_text(messages=[f"Your total of attempts: {player_attempts_count}",f"AI total of attempts: {ai_attempts_count}"])


def start_game(scores: Score) -> None:
    """
    Starting the game one time
    :param scores: a Score type param representing each score with his value
    :return: None
    """
    # Print game title and rules
    print_rules()

    #Get the entered number f values
    num_of_vals = get_num_of_values()

    #Get player list of numbers
    player_numbers = get_player_numbers(num_of_vals=num_of_vals)
    #Get AI list of numbers
    ai_numbers = get_ai_numbers(num_of_vals=num_of_vals)

    #Get player attempts count
    player_attempts_count = get_player_guesses(numbers_list=ai_numbers)
    #Get AI attempts count
    ai_attempts_count = get_ai_guesses(numbers_list=player_numbers)

    #Get and print results
    get_results(player_attempts_count=player_attempts_count, ai_attempts_count=ai_attempts_count, scores=scores)


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