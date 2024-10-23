def print_formated_text(message: str) -> None:
    message = f"      {message.capitalize()}      "
    top = f"┌{'─' * (len(message) - 2)}┐"
    bottom = f"└{'─' * (len(message) - 2)}┘"
    print(f"{top}\n{message}\n{bottom}")

def print_title(message: str = "Welcome To Guess The Sum") -> None:
    top = f"┌────────── {message.upper()} ──────────┐"
    message = f"      Welcome To {message.capitalize()}       "
    bottom = f"└{'─' * (len(message) - 2)}┘"
    print(f"{top}\n{message}\n{bottom}")
