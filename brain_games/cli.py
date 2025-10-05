import prompt


def welcome_user() -> str:
    player_name = prompt.string("May I have your name? ")

    if not isinstance(player_name, str):
        raise ValueError()

    print(f"Hello, {player_name}!")
    return player_name
