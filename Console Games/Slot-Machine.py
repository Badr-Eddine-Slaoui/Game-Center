"""
    Welcome to Slot Machine a simple gambling game
    Want to gamble without losing your money? very easy:
        -Enter your virtual balance (You can enter up t 1B$ !!!)
        -Then just start betting with each bet you'll spin a new row
        -If you hit the jackpot you'll receive your payout
        _If your balance run out the game will automatically stop
        _You can stop betting at anytime
        _At the end of each end you'll receive your results (final balance,scores)
        _Scores represent how much you won, you were close to won and how much the Slot Machin defeat you
    Warning: GAMBLING IS ADDICTED THIS JUST A GAME FOR FUN
"""


import random
from Utils import print_title, print_formated_text, get_scores, number_validation
from Types import Score, Strs


#Init symbols payouts multipliers and scores for both player an AI
SYMBOL_PAYOUTS = {
    "🍒": {"multiplier": 2, "player_score": 2, "ai_score": 1},
    "🍉": {"multiplier": 4, "player_score": 4, "ai_score": 3},
    "🍋": {"multiplier": 6, "player_score": 6, "ai_score": 5},
    "🔔": {"multiplier": 8, "player_score": 8, "ai_score": 7},
    "⭐": {"multiplier": 10, "player_score": 10, "ai_score": 8},
}


def print_rules() -> None:
    """
    Printing the game title and rules
    :return: None
    """
    #Print title
    print_title(title=f"python slots")
    #Print available symbols
    print_formated_text(messages=f"Symbols:🍉 │ ⭐ │ 🍋 │ 🔔 │ 🍒     ")
    #Print Rules
    print_formated_text(messages=f"""
    Welcome to Slot Machine a simple gambling game
    Want to gamble without losing your money? very easy:
        -Enter your virtual balance (You can enter up t 1B$ !!!)
        -Then just start betting with each bet you'll spin a new row
        -If you hit the jackpot you'll receive your payout
        _If your balance run out the game will automatically stop
        _You can stop betting at anytime 
        _At the end of each end you'll receive your results (final balance,scores) 
        _Scores represent how much you won, you were close to won and how much the Slot Machin defeat you
    Warning: GAMBLING IS ADDICTED THIS JUST A GAME FOR FUN
""")


def get_balance() -> int:
    """
    Get the balance of the player
    :return: an integer representing the balance
    """

    #Get a valid balance and return it
    return number_validation(prompt="Enter your balance (Between 100$ and 1B$): ",min_val=100,max_val=1000000000)


def get_bet(balance: int) -> int:
    """
    Get the bet of the player
    :param balance: an integer param representing the balance
    :return: an integer representing the bet
    """

    # Get a valid bet and return it
    return number_validation(prompt=f"Place your bet amount (Between 1$ and {balance}$): ",max_val=balance)


def spin_row() -> Strs:
    """
    Spin a new row nd return it
    :return: a Strs type representing the row symbols
    """
    #Start spinning
    print_formated_text(messages="Spinning...")
    #Init array of symbols
    symbols = ["🍉", "⭐", "🍋", "🔔", "🍒"]
    #Return three random choices
    return [random.choice(symbols) for _ in range(3)]


def print_row(row: Strs) -> None:
    """
    Print the row in the screen
    :param row: a Strs type param representing a row of 3 symbols
    :return: None
    """
    row_text = "  │  ".join(row)
    print_formated_text(messages=f"{row_text}   ")


def get_payout(row: Strs, bet: int, scores: Score) -> int:
    """
    Get the player payout and calculate and update scores
    :param row: a Strs type param representing a row of 3 symbols
    :param bet: an integer representing the player bet amount
    :param scores: a Score type representing the scores with their values
    :return: an integer representing the payout amount
    """

    #Init payout by 0
    payout = 0

    #If the three symbols are the same there's a payout other than that the payout will be 0$
    if row[0] == row[1] == row[2]:
        #Get the symbol
        symbol = row[0]
        #Check if the symbol exists in case of errors
        if symbol in SYMBOL_PAYOUTS:
            #Assign bet multiplied by the symbol multiplier to the payout
            payout = bet * SYMBOL_PAYOUTS[symbol]["multiplier"]
            #Update player score by adding the symbol player score
            scores["player_score"] += SYMBOL_PAYOUTS[symbol]["player_score"]
    #If there's just a two symbols match
    elif len(set(row)) == 2:
        #Get the matched symbol
        same_symbol =  row[0] if row[0] == row[1] or row[0] == row[2] else row[1]
        #Get the different symbol
        diff_symbol = row[2] if row[0] == row[1] else (row[0] if row[1] == row[2] else row[1])
        #Update player score by adding the same symbol player score
        scores["player_score"] += SYMBOL_PAYOUTS[same_symbol]["player_score"]
        # Update player score by adding the different symbol AI score
        scores["ai_score"] += SYMBOL_PAYOUTS[diff_symbol]["ai_score"]
    #In case of no match increment AI score by 1
    else:
        scores["ai_score"] += 1

    #Get payout result
    if payout > 0:
        result = f"Congrats you won a ${payout:,.2f}!!"
    else:
        result = "Sorry you lost this round!!"
    #Display payout result
    print_formated_text(messages=result)
    #return payout
    return payout


def print_result(start_balance: int,cur_balance: int) -> None:
    """
    Print the results of the game
    :param start_balance: an integer representing the player balance that he start with
    :param cur_balance: an integer representing the player current balance
    :return: None
    """
    #Print player results along with balance
    if cur_balance > start_balance:
        margin = cur_balance - start_balance
        result = f"Congratulation! You have win a margin of {margin}$,your finale balance is ${cur_balance:,.2f}"
    elif cur_balance > 0:
        result = f"Game over! You finale balance is ${cur_balance:,.2f}"
    else:
        result = "Game over! You Lost Everything"
    print_formated_text(messages=result)


def start_game(scores: Score) -> None:
    """
    Starting the game one time
    :param scores: a Score type param representing each score with his value
    :return: None
    """
    # Print game title and rules
    print_rules()
    # Get the entered balance
    origin_balance = cur_balance = get_balance()
    #The main loop for keep getting bets
    while True:
        #Print the current balance
        print_formated_text(messages=f"Current balance: ${cur_balance:,.2f}")
        #Get player bet
        bet = get_bet(balance=cur_balance)
        #Substract the bet from the current balance
        cur_balance -= bet
        #Spin a new row
        row = spin_row()
        #Print the row
        print_row(row=row)
        #Get player payout
        payout = get_payout(row=row, bet=bet, scores=scores)
        #Add the payout to the current balance
        cur_balance += payout
        #If the player choose to stop then stop the game
        if cur_balance == 0 or input("Do you want to spin again? (Y/N): ").upper() == "N":
            break
    #Print the game results
    print_result(start_balance=origin_balance,cur_balance=cur_balance)


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