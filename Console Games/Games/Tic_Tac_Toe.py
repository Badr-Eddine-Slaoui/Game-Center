"""
    Welcome to Tic Tac Toe a simple luck game
    I guess everyone knows how to play but in case u don't know:
        -Choose one symbols (either "X" or "O")
        -Whoever align three of his symbol in a straight horizontal, vertical or diagonal line wins
        _If the board fills up without any player meeting one of the winning conditions above, the game is a draw.
    Note: Don't choose the spots that already taken
"""


import random
from Utils import print_title, print_formated_text, get_scores, number_validation
from Types import Score, Screen, Spots, Nums
from typing import Dict, Tuple


def get_params() -> Dict[str,Screen | Nums | Nums | Spots | Score]:
    """
    Get the game require variables
    :return: a Dict representing the name and the value of each variable
    """

    #Return params in a dict
    return {
        #Represent the bord where players will play
        "screen": ["┌─────┐─────┌─────┐",
                   "│     │     │     │",
                   "│─────┘─────└─────│",
                   "│     │     │     │",
                   "│─────┐─────┌─────│",
                   "│     │     │     │",
                   "└─────┘─────└─────┘"],
        #Representing the index of the three lines of the screen
        "screen_lines_indexes": [1, 3, 5],
        #Representing the index of the middle of the three columns in a line
        "screen_cols_indexes": [3, 9, 15],
        #Representing each line with the already chose spots
        "lines_taken_spots": {
            1: [],
            3: [],
            5: []
        },
        #Represent the scores with their values
        "scores": {
            "player_score": 0,
            "ai_score": 0
        }
    }


def print_rules() -> None:
    """
    Printing the game title and rules
    :return: None
    """

    #Print game title
    print_title(title=f"Tic tac toe")
    #Print game rules
    print_formated_text(messages=f"""
    Welcome to Tic Tac Toe a simple luck game
    I guess everyone knows how to play but in case u don't know:
        -Choose one symbols (either "X" or "O")
        -Whoever align three of his symbol in a straight horizontal, vertical or diagonal line wins
        _If the board fills up without any player meeting one of the winning conditions above, the game is a draw.
    Note: Don't choose the spots that already taken
""")


def get_symbols() -> Tuple[str,str]:
    """
    Get player and AI symbols
    :return: a Tuple representing player and AI symbols
    """
    #Init symbols
    player_symbol = ai_symbol = ""
    #Get a valid choice from the player
    while True:
        player_symbol = input(f"Choose you symbol (X/O): ").upper()
        if player_symbol != "O" and player_symbol != "X":
            print_formated_text(messages=f"Invalid choice! Choose X or O")
        else:
            break

    #Assign the AI symbol depending on the player symbol
    ai_symbol = "X" if player_symbol == "O" else "O"
    #Return symbols
    return player_symbol, ai_symbol


def update_screen(line_choice: int, col_choice: int, lines_taken_spots: Spots, screen: Screen, symbol: str) -> None:
    """
    Update the screen with the new chosen spot
    :param line_choice: an integer param representing the index of the chosen line
    :param col_choice: an integer param representing the index of the chosen column
    :param lines_taken_spots: a Spots type param representing the already taken spots
    :param screen: a Screen type representing the game board
    :param symbol: a string param representing the player symbol
    :return: None
    """
    # Append the new spot to the line chosen spots list
    lines_taken_spots[line_choice].append(col_choice)
    # Create a new line from the chosen one
    new_line = list(screen[line_choice])
    # Replace the chosen spot with the player symbol
    new_line[col_choice] = symbol
    # Replace the chosen line with the new one
    screen[line_choice] = "".join(new_line)


def player_turn(screen_lines_indexes: Nums, screen_cols_indexes: Nums, lines_taken_spots: Spots,
                screen: Screen, player_symbol: str) -> None:
    """
    A new turn for the player in the game
    :param screen_lines_indexes: a Nums type param representing the indexes of the three line of the game board
    :param screen_cols_indexes: a Nums type param representing the indexes of the three column in a line
    :param lines_taken_spots: a Spots type param representing the already taken spots
    :param screen: a Screen type representing the game board
    :param player_symbol: a string param representing the player symbol
    :return: None
    """
    #Player turn
    while True:
        print_formated_text(messages=f"your turn",option="upper")
        #Get a valid line and column indexes from the player
        player_line_choice = screen_lines_indexes[number_validation(prompt="Enter line number (1,2,3): ",max_val=3) - 1]
        player_col_choice = screen_cols_indexes[number_validation(prompt="Enter column number (1,2,3): ",max_val=3) - 1]
        #Check if the chosen spot is available
        if player_col_choice not in lines_taken_spots[player_line_choice]:
            #Update the screen with the new chosen spot
            update_screen(line_choice=player_line_choice, col_choice=player_col_choice,
                          lines_taken_spots=lines_taken_spots, screen=screen, symbol=player_symbol)
            # Print the new screen
            print_screen(screen=screen)
            #Stop the loop
            break
        else:
            #Print an error message
            print_formated_text(messages=f"This slot is already taken!!")


def ai_turn(screen_lines_indexes: Nums, screen_cols_indexes: Nums, lines_taken_spots: Spots,
                screen: Screen, ai_symbol: str,player_symbol: str) -> None:
    """
    A new turn for the AI in the game
    :param screen_lines_indexes: a Nums type param representing the indexes of the three line of the game board
    :param screen_cols_indexes: a Nums type param representing the indexes of the three column in a line
    :param lines_taken_spots: a Spots type param representing the already taken spots
    :param screen: a Screen type representing the game board
    :param ai_symbol: a string param representing the AI symbol
    :param player_symbol: a string param representing the player symbol
    :return: None
    """

    #AI turn
    print_formated_text(messages=f"ai turn!!",option="upper")
    #Get the lines of the board
    line_one, line_two, line_three  = list(screen[1]) , list(screen[3]), list(screen[5])

    #Conditin the make the AI choice more accurate and win depending on the previous choices
    if (line_one[9] == line_one[15] == ai_symbol or
        line_two[3] == line_three[3] == ai_symbol or
        line_two[9] == line_three[15] == ai_symbol) and 3 not in lines_taken_spots[1]:
        line_one[3] = ai_symbol
        screen[1] = "".join(line_one)
        lines_taken_spots[1].append(3)

    elif (line_one[3] == line_one[15] == ai_symbol or
        line_two[9] == line_three[9] == ai_symbol) and 9 not in lines_taken_spots[1]:
        line_one[9] = ai_symbol
        screen[1] = "".join(line_one)
        lines_taken_spots[1].append(9)

    elif(line_one[3] == line_one[9] == ai_symbol or
        line_two[15] == line_three[15] == ai_symbol or
        line_two[9] == line_three[3] == ai_symbol) and 15 not in lines_taken_spots[1]:
        line_one[15] = ai_symbol
        screen[1] = "".join(line_one)
        lines_taken_spots[1].append(15)

    elif (line_two[9] == line_two[15] == ai_symbol or
        line_one[3] == line_three[3] == ai_symbol) and 3 not in lines_taken_spots[3]:
        line_two[3] = ai_symbol
        screen[3] = "".join(line_two)
        lines_taken_spots[3].append(3)

    elif (line_two[3] == line_two[15] == ai_symbol or
        line_one[9] == line_three[9] == ai_symbol or
        line_one[15] == line_three[3] == ai_symbol or
        line_one[3] == line_three[15] == ai_symbol) and 9 not in lines_taken_spots[3]:
        line_two[9] = ai_symbol
        screen[3] = "".join(line_two)
        lines_taken_spots[3].append(9)

    elif(line_two[3] == line_two[9] == ai_symbol or
        line_one[15] == line_three[15] == ai_symbol) and 15 not in lines_taken_spots[3]:
        line_two[15] = ai_symbol
        screen[3] = "".join(line_two)
        lines_taken_spots[3].append(15)

    elif (line_three[9] == line_three[15] == ai_symbol or
        line_two[3] == line_one[3] == ai_symbol or
        line_two[9] == line_one[15] == ai_symbol) and 3 not in lines_taken_spots[5]:
        line_three[3] = ai_symbol
        screen[5] = "".join(line_three)
        lines_taken_spots[5].append(3)

    elif (line_three[3] == line_three[15] == ai_symbol or
        line_two[9] == line_one[9] == ai_symbol) and 9 not in lines_taken_spots[5]:
        line_three[9] = ai_symbol
        screen[5] = "".join(line_three)
        lines_taken_spots[5].append(9)

    elif(line_three[3] == line_three[9] == ai_symbol or
        line_two[15] == line_one[15] == ai_symbol or
        line_two[9] == line_one[3] == ai_symbol) and 15 not in lines_taken_spots[5]:
        line_three[15] = ai_symbol
        screen[5] = "".join(line_three)
        lines_taken_spots[5].append(15)

    #Conditin the make the AI able to block the player if his about to win depending on the player previous choices
    elif (line_one[9] == line_one[15] == player_symbol or
        line_two[3] == line_three[3] == player_symbol or
        line_two[9] == line_three[15] == player_symbol) and 3 not in lines_taken_spots[1]:
        line_one[3] = ai_symbol
        screen[1] = "".join(line_one)
        lines_taken_spots[1].append(3)

    elif (line_one[3] == line_one[15] == player_symbol or
        line_two[9] == line_three[9] == player_symbol) and 9 not in lines_taken_spots[1]:
        line_one[9] = ai_symbol
        screen[1] = "".join(line_one)
        lines_taken_spots[1].append(9)

    elif(line_one[3] == line_one[9] == player_symbol or
        line_two[15] == line_three[15] == player_symbol or
        line_two[9] == line_three[3] == player_symbol) and 15 not in lines_taken_spots[1]:
        line_one[15] = ai_symbol
        screen[1] = "".join(line_one)
        lines_taken_spots[1].append(15)

    elif (line_two[9] == line_two[15] == player_symbol or
        line_one[3] == line_three[3] == player_symbol) and 3 not in lines_taken_spots[3]:
        line_two[3] = ai_symbol
        screen[3] = "".join(line_two)
        lines_taken_spots[3].append(3)

    elif (line_two[3] == line_two[15] == player_symbol or
        line_one[9] == line_three[9] == player_symbol or
        line_one[15] == line_three[3] == player_symbol or
        line_one[3] == line_three[15] == player_symbol) and 9 not in lines_taken_spots[3]:
        line_two[9] = ai_symbol
        screen[3] = "".join(line_two)
        lines_taken_spots[3].append(9)

    elif(line_two[3] == line_two[9] == player_symbol or
        line_one[15] == line_three[15] == player_symbol) and 15 not in lines_taken_spots[3]:
        line_two[15] = ai_symbol
        screen[3] = "".join(line_two)
        lines_taken_spots[3].append(15)

    elif (line_three[9] == line_three[15] == player_symbol or
        line_two[3] == line_one[3] == player_symbol or
        line_two[9] == line_one[15] == player_symbol) and 3 not in lines_taken_spots[5]:
        line_three[3] = ai_symbol
        screen[5] = "".join(line_three)
        lines_taken_spots[5].append(3)

    elif (line_three[3] == line_three[15] == player_symbol or
        line_two[9] == line_one[9] == player_symbol) and 9 not in lines_taken_spots[5]:
        line_three[9] = ai_symbol
        screen[5] = "".join(line_three)
        lines_taken_spots[5].append(9)

    elif(line_three[3] == line_three[9] == player_symbol or
        line_two[15] == line_one[15] == player_symbol or
        line_two[9] == line_one[3] == player_symbol) and 15 not in lines_taken_spots[5]:
        line_three[15] = ai_symbol
        screen[5] = "".join(line_three)
        lines_taken_spots[5].append(15)

    #If either player and AI aren't about to win choose a random choice
    else:
        #Get a spot that is not already taken
        while True:
            #Get a random line and column choice for the AI
            ai_line_choice = random.choice(screen_lines_indexes)
            ai_col_choice = random.choice(screen_cols_indexes)
            #Check spot availability
            if ai_col_choice not in lines_taken_spots[ai_line_choice]:
                # Update the screen with the new chosen spot
                update_screen(line_choice=ai_line_choice, col_choice=ai_col_choice,
                              lines_taken_spots=lines_taken_spots, screen=screen, symbol=ai_symbol)
                #Stop the loop
                break
    # Print the new screen
    print_screen(screen=screen)


def print_screen(screen: Screen) -> None:
    """
    Print the screen line by line
    :param screen: a Screen type representing the game board
    :return: None
    """

    #Print the screen line by line
    for line in screen:
        print(line)


def check_results(screen: Screen,lines_taken_spots: Spots,player_symbol: str, ai_symbol: str, game_running: bool, scores: Score) -> bool:
    """
    Check the game results if there's a winner or the board is fills up to stop the game other that continue playing
    :param screen: a Screen type representing the game board
    :param lines_taken_spots: a Spots type param representing the already taken spots
    :param player_symbol: a string param representing the player symbol
    :param ai_symbol: a string param representing the AI symbol
    :param game_running: a boolean param representing the condition of the game
    :param scores: a Score type param representing each score with his value
    :return: a boolean param representing the condition of the game
    """

    # Get the lines of the board
    line_one, line_two, line_three = list(screen[1]), list(screen[3]), list(screen[5])

    #If the player has a straight horizontal, vertical or diagonal line win
    if (line_one[3] == line_one[9] == line_one[15] == player_symbol or
        line_two[3] == line_two[9] == line_two[15] == player_symbol or
        line_three[3] == line_three[9] == line_three[15] == player_symbol or
        line_one[3] == line_two[3] == line_three[3] == player_symbol or
        line_one[9] == line_two[9] == line_three[9] == player_symbol or
        line_one[15] == line_two[15] == line_three[15] == player_symbol or
        line_one[3] == line_two[9] == line_three[15] == player_symbol or
        line_one[15] == line_two[9] == line_three[3] == player_symbol):
        #Print win message
        print_formated_text(messages=f"Congrats! You Win!!!")
        #Incremet player score by 1
        scores["player_score"] += 1
        #Stop the game
        game_running = False
    # If the AI has a straight horizontal, vertical or diagonal line player lose
    elif (line_one[3] == line_one[9] == line_one[15] == ai_symbol or
        line_two[3] == line_two[9] == line_two[15] == ai_symbol or
        line_three[3] == line_three[9] == line_three[15] == ai_symbol or
        line_one[3] == line_two[3] == line_three[3] == ai_symbol or
        line_one[9] == line_two[9] == line_three[9] == ai_symbol or
        line_one[15] == line_two[15] == line_three[15] == ai_symbol or
        line_one[3] == line_two[9] == line_three[15] == ai_symbol or
        line_one[15] == line_two[9] == line_three[3] == ai_symbol):
        #Print the loose message
        print_formated_text(messages=f"Game Over! You lost!!")
        #Increment AI score by 1
        scores["ai_score"] += 1
        #Stop the game
        game_running = False

    else:
        #If no one win check if the board is fills up
        if len(lines_taken_spots[1]) == len(lines_taken_spots[3]) == len(lines_taken_spots[5]) == 3:
            #If it is print a tie message
            print_formated_text(messages=f"Game Over! It's a Tie!!")
            #Stop the game
            game_running = False

    #Other than that continue the game

    #Return the condition of the game
    return game_running


def start_game(scores: Score) -> None:
    """
    Starting the game one time
    :param scores: a Score type param representing each score with his value
    :return: None
    """

    #Init game require variables
    params = get_params()
    screen = params["screen"]
    screen_lines_indexes = params["screen_lines_indexes"]
    screen_cols_indexes = params["screen_cols_indexes"]
    lines_taken_spots = params["lines_taken_spots"]
    game_running = True
    # Print game title, rules and screen
    print_rules()
    print_screen(screen)
    #Get player and AI symbols
    player_symbol, ai_symbol = get_symbols()
    #Game main loop
    while game_running:
        #Take a new player turn
        player_turn(screen_lines_indexes=screen_lines_indexes, screen_cols_indexes=screen_cols_indexes,
                    lines_taken_spots=lines_taken_spots, screen=screen, player_symbol=player_symbol)
        #Check if there's a results after turn
        game_running = check_results(screen=screen, lines_taken_spots=lines_taken_spots,player_symbol=player_symbol,
                                     ai_symbol=ai_symbol,game_running=game_running,scores=scores)
        #Stop the game if there's a results
        if not game_running:
            break
        #Take a new AI turn
        ai_turn(screen_lines_indexes=screen_lines_indexes, screen_cols_indexes=screen_cols_indexes,
                lines_taken_spots=lines_taken_spots, screen=screen,ai_symbol=ai_symbol,player_symbol=player_symbol)
        # Check if there's a results after turn
        game_running = check_results(screen=screen, lines_taken_spots=lines_taken_spots, player_symbol=player_symbol,
                                     ai_symbol=ai_symbol, game_running=game_running, scores=scores)


def main() -> None:
    """
    The main function of the programme
    :return: None
    """

    # Init scores
    scores = get_params()["scores"]

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