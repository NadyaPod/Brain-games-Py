import prompt


def welcome_user():
    player_name = prompt.string("May I have your name? ")
    print(f"Hello, {player_name}!")
    return player_name
