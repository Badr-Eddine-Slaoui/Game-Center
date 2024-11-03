from Models.Database import Database
from Models.Player import Player
from Utils import print_title, print_formated_text, number_validation
from Games.Dice_Roller import main as Dice_Roller
from Games.Guess_The_Sum import main as Guess_The_Sum
from Games.Rock_Paper_Scissors import main as Rock_Paper_Scissors
from Games.Slot_Machine import main as Slot_Machine
from Games.Tic_Tac_Toe import main as Tic_Tac_Toe


def validate_username():
    while True:
        username = input(f"Enter a three character username: ")
        if not username:
            err = "Username is require"
        elif len(username) != 3:
            err = f"Username should be three characters!!"
        else:
            break
        print_formated_text(messages=err)
    return username


def validate_password(confirm: bool = False):
    while True:
        password = input(f"Enter your password: ")
        if password == "":
            print_formated_text(messages=f"Password is required")
        else:
            break
    while confirm:
        confirm_password = input(f"Confirm your password: ")
        if confirm_password == "":
            err = f"Password confirmation is required"
        elif password != confirm_password:
            err = f"Password and password confirmation should be the same"
        else:
            break
        print_formated_text(messages=err)
    return password


def register(session):
    player = None
    print_formated_text(messages=[f"Hello New Gamer!!",f"Please fill up this infos so we can create your gaming account"])
    username = validate_username()
    password = validate_password(confirm=True)
    player = Player.register(session=session,username=username,password=password)
    return player

def login(session):
    player = None
    print_formated_text(messages=[f"Sup Gamer!!", f"Please fill up this infos to login"])
    username = validate_username()
    password = validate_password()
    player = Player.login(session=session, username=username, password=password)
    return player

def main():
    print_title(title=f"Game center")
    player = None
    db = Database()
    with db.get_session() as session:
        while True:
            print_formated_text(messages=[f"Choose one of this choices:", f"1- SignUp", "2- Login", "3- Quit"])
            choice = number_validation(prompt=f"Please enter your choice: ", max_val=3)

            match choice:
                case 1:
                    player = register(session=session)
                    if player:
                        print_formated_text(
                            messages=f"A new GAMER landed!! Welcome to your new family {player.username}")
                        player.recharge_balance(session=session, player=player,
                                                prompt=f"Please enter your balance so u can play (Between 5$ and 1B$): ")
                        break
                case 2:
                    player = login(session=session)
                    if player:
                        print_formated_text(messages=f"Welcome Home {player.username}")
                        player.check_balance(session=session, player=player)
                        break
                case 3:
                    print_formated_text(messages=f"GoodBye Soldier!")
                    exit(0)
                case _:
                    print_formated_text(messages=f"Invalid!!")

        if player.is_logged:
            while True:
                print_formated_text(
                    messages=[f"Choose your game", f"1- Dice Roller", f"2- Guess The Sum", f"3- Rock Paper Scissors",
                              f"4- Slot Machine", f"5- Tic Tac Toe", f"6- Quit"])
                game_choice = number_validation(prompt=f"What do you want to play today? ", max_val=6)
                match game_choice:
                    case 1:
                        Dice_Roller()
                    case 2:
                        Guess_The_Sum()
                    case 3:
                        Rock_Paper_Scissors()
                    case 4:
                        Slot_Machine()
                    case 5:
                        Tic_Tac_Toe()
                    case 6:
                        print_formated_text(messages=f"GoodBye Soldier!")
                        exit(0)
                    case _:
                        print_formated_text(messages=f"Invalid Game!!")


if __name__ == "__main__":
    main()